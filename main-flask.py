from dataclasses import dataclass

from flask import render_template, Flask


@dataclass
class User:
    name: str
    age: int
    address: str
    phone: str


def main():
    app = Flask(__name__)
    user1 = User("Marcin", 49, "ul. Firleja 24", "692-26-88-99")
    user2 = User("Dominika", 47, "ul. Firleja 24", "532-488-338")

    users = [user1, user2]
    with app.app_context():
        result = render_template("bootstrap_table.html", title="Marcin demo", users=users)
    with open("Result-bootstrap-table.html", "wt") as file:
        file.write(result)


if __name__ == '__main__':
    main()
