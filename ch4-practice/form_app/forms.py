from django import forms

# 예제 4-18
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

'''
예제 4-19 : 위 NameForm 클래스를 form 변수로 전달해서 템플릿 코드를 렌더링한 결과

<label for="your_name">Your Name: </label>
<input id="your_name" type="text" name="your_name" max_length="100">

'''


# 예제 4-22
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

'''
예제 4-23 : 위의 ContactForm 폼 클래스를 form 변수로 전달해서 {{ form.as_p }} 옵션의 템플릿 코드를 렌더링한 결과

<p><label for="id_subject">Subject</label>
    <input id="id_subject" type="text" name="subject" maxlength="100" /></p>
<p><label for="id_message">Message</label>
    <input type="text" name="subject" id="id_message" /></p>
<p><label for="id_sender">Sender</label>
    <input type="email" name="sender" id="id_sender" /></p>
<p><label for="id_cc_myself">Cc myself</label>
    <input type="checkbox" name="cc_myself" id="id_cc_myself" /></p>
 
'''