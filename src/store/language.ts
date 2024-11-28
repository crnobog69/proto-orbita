type SupportedLanguage = "en" | "sr";

interface Translation {
  [key: string]: {
    [lang: string]: {
      [key: string]: string;
    };
  };
}

export const translations: Translation = {
  nav: {
    en: {
      title: "Proto Orbit",
      github: "GitHub Profile",
      theme: "Toggle theme",
      language: "Language",
    },
    sr: {
      title: "Прото Орбита",
      github: "GitHub Профил",
      theme: "Промени тему",
      language: "Језик",
    },
  },
  blog: {
    en: {
      readMore: "Read more",
      backToHome: "← Back",
    },
    sr: {
      readMore: "Прочитај више",
      backToHome: "← Назад",
    },
  },
  languages: {
    en: {
      en: "English",
      sr: "Serbian Cyrillic",
    },
    sr: {
      en: "Енглески",
      sr: "Српска ћирилица",
    },
  },
};

export const defaultLanguage: SupportedLanguage = "en";

export function getCurrentLanguage(): SupportedLanguage {
  if (typeof localStorage !== "undefined") {
    const savedLang = localStorage.getItem("language") as SupportedLanguage;
    if (savedLang && (savedLang === "en" || savedLang === "sr")) {
      return savedLang;
    }
  }
  return defaultLanguage;
}

export function translate(section: string, key: string): string {
  const currentLang = getCurrentLanguage();
  const translation = translations[section]?.[currentLang]?.[key];
  return translation || key;
}
