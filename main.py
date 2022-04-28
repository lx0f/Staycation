from record import Record
from cli import CLI
from ui import UI

record_list = [
    Record("apple", "aaa", 10, 900),
    Record("banana", "cdd", 10, 79),
    Record("caremel", "aab", 10, 23),
    Record("durian", "bbb", 10, 3),
    Record("ice cream", "ccc", 10, 50),
    Record("vanilla", "bbc", 10, 39),
    Record("zoro", "ccd", 10, 100),
    Record("sugar", "ddd", 10, 397),
    Record("xeno", "abb", 10, 42),
    Record("hugo", "bcc", 10, 69),
]

cli = CLI(record_list)
ui = UI()


if __name__ == "__main__":
    while cli.run:
        cli.display_actions()
        action_id = ui.input_lambda(cli.is_valid_action, int, "Enter action id: ")
        cli.run_action(action_id)
