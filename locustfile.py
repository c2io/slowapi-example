from locust import HttpUser, task, between  # noqa
from locust.contrib.fasthttp import FastHttpUser


class LimitedUser(FastHttpUser):
    @task
    def get_root(self):
        response = self.client.get("/")  # noqa: F841

    # wait_time = between(2, 3)
