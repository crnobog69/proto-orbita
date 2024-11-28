type Language = "en" | "sr";

let currentLanguage: Language = "sr";

export function getCurrentLanguage(): Language {
  return currentLanguage;
}

export function setLanguage(lang: Language) {
  currentLanguage = lang;
}

export function translate(key: string): string {
  // Add translations here
  const translations: Record<Language, Record<string, string>> = {
    en: {
      // English translations
    },
    sr: {
      // Serbian translations
    },
  };

  return translations[currentLanguage][key] || key;
}
