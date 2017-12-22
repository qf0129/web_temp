from locust import HttpLocust, TaskSet, task

def login(l):
    l.client.post("/admin", {"username":"admin", "password":"bowheadhome"})

def index(l):
    l.client.get("/")

def product(l):
    l.client.get("/product")

def faq(l):
    l.client.get("/faq")

def blog(l):
    l.client.get("/blog")


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.post("/admin", {"username":"admin", "password":"bowheadhome"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def product(self):
        self.client.get("/product")

    @task(3)
    def faq(self):
        self.client.get("/faq")

    @task(4)
    def blog(self):
        self.client.get("/blog")

    @task(5)
    def blog(self):
        self.client.get("/setup")

    @task(6)
    def blog(self):
        self.client.get("/support")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
