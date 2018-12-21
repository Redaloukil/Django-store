from allauth.account.forms import LoginForm

class LoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.
        
        # You must return the original result.
        return super(LoginForm, self).login(*args, **kwargs)