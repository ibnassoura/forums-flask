from flask import Flask, render_template, request, redirect
from app import models
from app import stores
from app import dummy_data
from views import *


post_store = stores.PostStore()
member_store = stores.MemberStore()


if __name__  == "__main__":
    dummy_data.seed_stores(member_store, post_store)
    app.run()


