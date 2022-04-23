class signupuserForm(forms.ModelForm):
    class Meta:
        model = signupuser
        fields = ['uid','uname','umail','pwd','filename','filepath']