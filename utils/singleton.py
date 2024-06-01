import streamlit as st

# Extracted from https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-singleton-in-python#:~:text=Method%203%3A%20A%20metaclass

class Singleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        object_in_state = st.session_state.get(cls, None)
        if object_in_state is None:
            st.session_state[cls] = cls

        instances = []
        if object_in_state is not None:
            instances = object_in_state.instances

        if cls not in instances:
            st.session_state[cls].instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return st.session_state[cls].instances[cls]


# USAGE:
# class MyClass(BaseClass, metaclass=Singleton):
#    pass