from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        user = self.get_one(user.get("id"))
        user.username = user.get("username")
        user.password = user.get("password")

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()

