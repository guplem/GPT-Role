import streamlit as st

# Extracted from https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-singleton-in-python#:~:text=Method%203%3A%20A%20metaclass

class Singleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        obj = st.session_state.get(cls, None)
        if obj is None:
            st.session_state[cls] = cls

        instances = []
        if obj is not None:
            instances = obj.instances

        if cls not in instances:
            st.session_state[cls].instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return st.session_state[cls].instances[cls]


# USAGE:
# class MyClass(BaseClass, metaclass=Singleton):
#    pass