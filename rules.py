class KYNI_Lovers_Rules:
    """
    KYNI Lovers Rules: Stay productive, stay comfortable, stay KYNI.
    """

    RULES = [
        "1. Нікому не розповідати про 'KYNI lovers'.",
        "2. Ніколи нікому не розповідати про 'KYNI lovers'.",
        "3. Якщо прод падає, API не відповідає, або продакшн горить — "
        "роботу зупиняємо й рефакторимо.",
        "4. У кожному pull request бере участь лише один кодер.",
        "5. Не більше одного критичного багу за раз — багтрекер не гумовий.",
        "6. Кодимо без зайвого формалізму — лише комфорт і продуктивність.",
        "7. Рев'ю триває стільки, скільки потрібно, щоб знайти всі баги.",
        "8. Джун зобов'язаний фіксити баги.",
    ]

    SPECIAL_NOTE = (
        "Всі задачі в backlog'у — рівні. "
        "Але деякі рівніші за інші."
    )

    @staticmethod
    def print_rules():
        """
        Виводить правила KYNI lovers.
        """
        print("=== KYNI LOVERS RULES ===")
        for rule in KYNI_Lovers_Rules.RULES:
            print(rule)
        print("\n***")
        print(KYNI_Lovers_Rules.SPECIAL_NOTE)
        print("***")


if __name__ == "__main__":
    # Показати правила на сервері
    KYNI_Lovers_Rules.print_rules()