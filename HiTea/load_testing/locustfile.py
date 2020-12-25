from locust import HttpUser, TaskSet, task


# class UserBehavior(TaskSet):
#     @task
#     def index(self):
#         self.client.get('/')

    # @task
    # def menu(self):
    #     self.client.get('/menu')


class WebsiteUser(HttpUser):
    @task
    def index(self):
        self.client.get('/menu')


    min_wait = 500
    max_wait = 5000