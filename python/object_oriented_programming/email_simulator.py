from __future__ import annotations
from datetime import UTC, datetime


class Email:
    def __init__(self, sender: str, receiver: str, subject: str, body: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.now(UTC)
        self.read = False

    def mark_as_read(self) -> None:
        self.read = True

    def display_email(self) -> str:
        self.mark_as_read()
        heading = ' Email '

        return (
            f'\n{heading:-^30}\n\n'
            f'From: {self.sender.name}\n'
            f'To: {self.receiver.name}\n'
            f'Subject: {self.subject}\n'
            f'Received: {self.timestamp.strftime("%Y-%m-%d %H:%M")}\n'
            f'\n{self.body}\n'
            f'\n{"-" * 30}\n'
        )

    def __str__(self) -> str:
        status = 'Read' if self.read else 'Unread'

        return f'[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime("%Y-%m-%d %H:%M")}'


class Inbox:
    def __init__(self):
        self.emails: list[Email] = []

    def receive_email(self, email: Email) -> None:
        self.emails.append(email)

    def view_emails(self) -> str:
        if not self.emails:
            return 'No emails.'

        headline = 'Your Emails:\n'
        email_list = []

        for i, email in enumerate(self.emails, start=1):
            email_list.append(f'\n{i}. {email}\n')

        return headline + ' '.join(email_list)

    def read_email(self, index: int) -> str:
        if not self.emails:
            return 'Inbox is empty.'

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            return 'Email not found.'

        return self.emails[actual_index].display_email()

    def delete_email(self, index: int) -> str:
        if not self.emails:
            return 'Inbox is already empty.'

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            return 'Email not found.'

        del self.emails[actual_index]
        return 'Email deleted.'


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver: User, subject: str, body: str) -> None:
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)

    def check_inbox(self) -> str:
        headline = f" {self.name}'s Inbox "
        return f'{headline:-^30}\n\n' + self.inbox.view_emails()

    def read_email(self, index: int) -> str:
        return self.inbox.read_email(index)

    def delete_email(self, index: int) -> str:
        return self.inbox.delete_email(index)


alice = User('Alice')
bob = User('Bob')

alice.send_email(bob, 'Vacation', "I've found us a perfect spot!")

assert len(bob.inbox.emails) == 1
assert bob.inbox.emails[0].subject == 'Vacation'
assert not bob.inbox.emails[0].read

email = bob.read_email(1)

assert 'From: Alice' in email
assert 'Subject: Vacation' in email
assert bob.inbox.emails[0].read

bob.send_email(alice, 'Re: Vacation', 'Booking it right now!')

assert len(alice.inbox.emails) == 1

alice.delete_email(1)

assert len(alice.inbox.emails) == 0
