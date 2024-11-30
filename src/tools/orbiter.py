from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, 
                            QMessageBox, QStatusBar)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QClipboard
from datetime import datetime, timezone
import yaml
from pathlib import Path
import sys

class BlogManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Орбитер - Прото Орбита")
        self.setMinimumSize(800, 600)
        
        # Get clipboard
        self.clipboard = QApplication.clipboard()
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Title input
        title_layout = QHBoxLayout()
        title_label = QLabel("Наслов:")
        self.title_entry = QLineEdit()
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.title_entry)
        layout.addLayout(title_layout)
        
        # Excerpt input
        excerpt_layout = QHBoxLayout()
        excerpt_label = QLabel("Кратак опис:")
        self.excerpt_entry = QLineEdit()
        excerpt_layout.addWidget(excerpt_label)
        excerpt_layout.addWidget(self.excerpt_entry)
        layout.addLayout(excerpt_layout)
        
        # Content input
        content_label = QLabel("Садржај:")
        self.content_text = QTextEdit()
        layout.addWidget(content_label)
        layout.addWidget(self.content_text)
        
        # Buttons
        button_layout = QHBoxLayout()
        create_button = QPushButton("Креирај објаву")
        clear_button = QPushButton("Очисти")
        copy_button = QPushButton("Копирај у међуспремник")
        
        create_button.clicked.connect(self.create_post)
        clear_button.clicked.connect(self.clear_fields)
        copy_button.clicked.connect(self.copy_to_clipboard)
        
        button_layout.addWidget(create_button)
        button_layout.addWidget(clear_button)
        button_layout.addWidget(copy_button)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        # Set style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e24;
                color: #f7ebe8;
            }
            QLabel {
                color: #f7ebe8;
            }
            QLineEdit, QTextEdit {
                background-color: #2a2a32;
                color: #f7ebe8;
                border: 1px solid #e54b4b;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #e54b4b;
                color: #f7ebe8;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #ffa987;
            }
            QStatusBar {
                background-color: #2a2a32;
                color: #f7ebe8;
            }
        """)

    def create_post(self):
        title = self.title_entry.text().strip()
        excerpt = self.excerpt_entry.text().strip()
        content = self.content_text.toPlainText().strip()
        
        if not all([title, excerpt, content]):
            QMessageBox.critical(self, "Error", "Сва поља су обавезне!")
            return
            
        try:
            # Create slug from title
            slug = self._create_slug(title)
            
            # Create frontmatter data
            frontmatter_data = {
                'title': title,
                'pubDate': datetime.now(timezone.utc).isoformat(),
                'excerpt': excerpt
            }
            
            # Format the markdown file content
            file_content = "---\n"
            file_content += yaml.dump(frontmatter_data, allow_unicode=True, default_flow_style=False)
            file_content += "---\n\n"
            file_content += content
            
            # Get the blog directory path
            blog_dir = Path(__file__).parent.parent.parent / "src" / "content" / "blog"
            
            # Create file path
            file_path = blog_dir / f"{slug}.md"
            
            # Save the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
            
            self.statusBar.showMessage(f"Објава успешно креирана: {file_path}")
            QMessageBox.information(self, "Success", "Објава успешно креирана!")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Неуспешно креирање објаве: {str(e)}")
            
    def clear_fields(self):
        self.title_entry.clear()
        self.excerpt_entry.clear()
        self.content_text.clear()
        self.statusBar.clearMessage()

    def copy_to_clipboard(self):
        content = self.content_text.toPlainText()
        self.clipboard.setText(content)
        self.statusBar.showMessage("Садржај копиран у међуспремник!")
        # Clear status message after 2 seconds
        QTimer.singleShot(2000, self.statusBar.clearMessage)
        
    def _create_slug(self, title):
        # Simple slug creation - replace spaces with hyphens and lowercase
        slug = title.lower().replace(" ", "-")
        # Remove any non-alphanumeric characters (except hyphens)
        slug = "".join(c for c in slug if c.isalnum() or c == "-")
        return slug

def main():
    app = QApplication(sys.argv)
    window = BlogManager()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 