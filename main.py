import json

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class CircularAvatarImage(MDCard):
    avatar = StringProperty()
    name = StringProperty()


class StoryCreator(MDCard):
    avatar = StringProperty()


class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    posted_ago = StringProperty()


class HomePage(MDScreen):
    profile_picture = 'https://avatars.githubusercontent.com/u/89080192?v=4'

    def on_enter(self):
        self.list_stories()
        self.list_posts()

    def list_stories(self):
        with open('assets/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar=data[name]['avatar'],
                    name=name,
                ))

    def list_posts(self):
        with open('assets/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username=username,
                    avatar=data[username]['avatar'],
                    profile_pic=self.profile_picture,
                    post=data[username]['post'],
                    caption=data[username]['caption'],
                    likes=data[username]['likes'],
                    comments=data[username]['comments'],
                    posted_ago=data[username]['posted_ago']
                ))


class MainApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        Builder.load_file('home_page.kv')
        return HomePage()

    def on_start(self):
        self.root.dispatch('on_enter')


if __name__ == "__main__":
    MainApp().run()
