---
excerpt: Једноставно компајлирање C програма
pubDate: '2024-11-30T18:12:29.942507+00:00'
title: 3 | Compile, Run, C
---

## Брзо и једноставно.

```bash
chmod +x crc.sh
```

```c
#!/bin/bash

# Боје
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
PEACH='\033[38;2;250;183;135m'
LAVANDER='\033[38;2;180;191;254m'
RESET='\033[0m'

# Функција за проверу грешака
check_error() {
    if [ $? -ne 0 ]; then
        echo -e "${RED}Грешка: $1${NC}"
        return 1
    fi
    return 0
}

# Проверимо да ли је аргумент прослеђен
if [ -z "$1" ]; then
    echo -e "${RED}Унесите име датотеке са .c на крају!${RESET}"
    echo "Пример коришћења: ./crc.sh program.c -lm"
    echo -e "${YELLOW}За помоћ укуцати ./crc.sh --help${RESET}"
    exit 1
fi

# Ако је корисник унео --help, приказујемо помоћ
if [ "$1" == "--help" ]; then
    echo "==================================================================="
    echo
    echo -e "${RED} Алат за једноставно компајлирање програма написаних у 'C'.${RESET}"
    echo
    echo -e "${CYAN} 'crc.sh'${RESET} ${RED}Скрипта | Помоћ${RESET} ${CYAN}(Compile, Run, C)${RESET}"
    echo
    echo "==================================================================="    
    echo
    echo -e "${YELLOW} Коришћење:${RESET}"
    echo
    echo -e "${CYAN}   ./crc.sh${RESET} ${LAVANDER}ime_datoteke.c${RESET} ${PEACH}додатне_опције${RESET}"
    echo
    echo -e "${YELLOW} Опис:${RESET}"
    echo
    echo "  Овај алат компајлира програме написане у C и поседује опцију"
    echo "  додавања библиотеке ако је потребно."
    echo
    echo -e "${RED}  Пример 1:${RESET} ${CYAN}./crc.sh${RESET} ${LAVANDER}program.c${RESET}"
    echo -e "${RED}  Пример 2:${RESET} ${CYAN}./crc.sh${RESET} ${LAVANDER}program.c${RESET} ${PEACH}-lm -lncurses${RESET}"
    echo -e "${RED}  Пример 3:${RESET} ${CYAN}./crc.sh${RESET} ${LAVANDER}program.c${RESET} ${PEACH}-lm${RESET}"
    echo
    echo "==================================================================="
    echo
    echo -e "${YELLOW} Додатне опције:${RESET}"
    echo
    echo -e "  ${PEACH}--help${RESET}        Приказује ову помоћ."
    echo -e "  ${PEACH}-lm${RESET}           Додаје математичку библиотеку."
    echo -e "  ${PEACH}-lncurses${RESET}     Додаје библиотеку за рад са терминалом."
    echo -e "  ${PEACH}-lpthread${RESET}     Додаје библиотеку за рад са нитима."
    echo
    echo -e "  Или нека друга библиотека, исто као ${RED}'gcc'${RESET} компајлер."
    echo
    echo "==================================================================="
    exit 0
fi

# Име датотеке са екстензијом
FILE=$1

# Проверимо да ли датотека има .c екстензију
if [[ "$FILE" != *.c ]]; then
    echo -e "${RED}Унесите име датотеке са .c на крају!${RESET}"
    echo -e "${YELLOW}За помоћ укуцати ./crc.sh --help${RESET}"
    exit 1
fi

# Уклонити .c екстензију да добијемо име извршне датотеке
FILENAME=${FILE%.c}

# Додатне библиотеке (ако постоје)
shift # Уклонити први аргумент (име фајла)
LIBRARIES=$@

# Компилација са додатним библиотекама
echo -e "${CYAN}Компајлирање...${RESET}"
gcc "$FILE" -o "$FILENAME" $LIBRARIES
if [ $? -ne 0 ]; then
    echo -e "${RED}Грешка приликом компајлирања!${RESET}"
    echo -e "${YELLOW}За помоћ укуцати ./crc.sh --help${RESET}"
    exit 1
fi

# Покретање извршне датотеке
echo -e "${GREEN}Покретање извршне датотеке: ./${FILENAME}${RESET}"
echo "--------------------------" 
echo
./"$FILENAME"
```