# Курсовая работа №4 ООП

## Получение вакансий от платформ работодателей

### Особенности проекта
- Получение вакансий по API с платформ HeadHunter и SuperJob
  (имеется возможность для рсасширения списка платформ)
- проект создан в виртуальной среде poetry

### Краткое описание проекта:
- В директории classes расположеенны все используемые классы
- В директории utils расположеенны все используемые функции
- В директории data по завершении работы программы формируется файл с отсортированными вакансиями

#### Описание работы программы:
- После запуска фала main пользователю предлогается ввести данные для поиска вакансий
- Получив данные программа обращается к платформам через API с учетом фильтров поиска
- По каждой платформе формируется список экземмляров классов (списки вакансий) с общими отрибутами для всех классов
- Формируется общий список экземмляров классов (списки вакансий)
- Список фильтруется с учетом ключевых слов по условию требований к вакансии и по заработной плате
- Список, отфильтрованных вакансий, сохраняется в файл
- Список, отфильтрованных вакансий, выводится пользователю в консоль с учетом top_n