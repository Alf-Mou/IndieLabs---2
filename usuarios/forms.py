from django import forms

class LoginForms(forms.Form):
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form__input",
                "placeholder": "Email"
            }
        )
    )

    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form__input",
                "placeholder": "Senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_completo=forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
                widget=forms.TextInput(
            attrs={
                "class": "form__input",
                "placeholder": "Nome completo"
            }
        )
    )


    pais = forms.ChoiceField(
        label="País",
        required=True,
        choices=[('', 'Selecione um país')],  
        widget=forms.Select(
            attrs={
                "id": "country",
                "class": "form__select",
                "placeholder": "Selecione um país"
            }
        )
    )

    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form__input",
                "placeholder": "Email"
            }
        )
    )

    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form__input",
                "placeholder": "Senha"
            }
        )
    )