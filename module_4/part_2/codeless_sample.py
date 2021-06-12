{
  "id": "20b2e155-3e14-4101-9c25-8596b1f79bea",
  "version": "2.0",
  "name": "test_user_registration",
  "url": "http://selenium1py.pythonanywhere.com",
  "tests": [{
    "id": "f2aa83a2-abe1-45c1-87e3-373427fabcb1",
    "name": "registration",
    "commands": [{
      "id": "1c09b3c7-5d1b-4d06-bbd3-7941351dfebb",
      "comment": "",
      "command": "open",
      "target": "/ru/",
      "targets": [],
      "value": ""
    }, {
      "id": "ce453300-bcdc-4bca-b0fe-478bc008c21c",
      "comment": "",
      "command": "setWindowSize",
      "target": "968x984",
      "targets": [],
      "value": ""
    }, {
      "id": "e2b52c30-e17d-4352-bc0f-7bfc46e8ab6f",
      "comment": "",
      "command": "click",
      "target": "id=login_link",
      "targets": [
        ["id=login_link", "id"],
        ["linkText=Войти или зарегистрироваться", "linkText"],
        ["css=#login_link", "css:finder"],
        ["xpath=//a[contains(text(),'Войти или зарегистрироваться')]", "xpath:link"],
        ["xpath=//a[@id='login_link']", "xpath:attributes"],
        ["xpath=//div[@id='top_page']/div[2]/div/ul/li/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/ru/accounts/login/')]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,' Войти или зарегистрироваться')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "cdfce7f5-e629-4f83-b2e6-8098d80633d1",
      "comment": "",
      "command": "click",
      "target": "id=id_registration-email",
      "targets": [
        ["id=id_registration-email", "id"],
        ["name=registration-email", "name"],
        ["css=#id_registration-email", "css:finder"],
        ["xpath=//input[@id='id_registration-email']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "53916e56-3c19-4dc3-bab5-580ccde925ae",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-email",
      "targets": [
        ["id=id_registration-email", "id"],
        ["name=registration-email", "name"],
        ["css=#id_registration-email", "css:finder"],
        ["xpath=//input[@id='id_registration-email']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div/div/input", "xpath:position"]
      ],
      "value": "spasovevgeniy@gmail.com"
    }, {
      "id": "982d8e09-ec21-40fc-803b-e926a2a5d420",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-password1",
      "targets": [
        ["id=id_registration-password1", "id"],
        ["name=registration-password1", "name"],
        ["css=#id_registration-password1", "css:finder"],
        ["xpath=//input[@id='id_registration-password1']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/form/div[2]/div/input", "xpath:position"]
      ],
      "value": "Poiuytrewqaz1!"
    }, {
      "id": "c05c897a-fa49-46c9-8e1f-4b576d68ec7b",
      "comment": "",
      "command": "click",
      "target": "id=id_registration-password2",
      "targets": [
        ["id=id_registration-password2", "id"],
        ["name=registration-password2", "name"],
        ["css=#id_registration-password2", "css:finder"],
        ["xpath=//input[@id='id_registration-password2']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d9ca805d-dbc4-4dcb-bf04-502b7a5a0d8c",
      "comment": "",
      "command": "type",
      "target": "id=id_registration-password2",
      "targets": [
        ["id=id_registration-password2", "id"],
        ["name=registration-password2", "name"],
        ["css=#id_registration-password2", "css:finder"],
        ["xpath=//input[@id='id_registration-password2']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": "Poiuytrewqaz1!"
    }, {
      "id": "3afc819a-7d0b-4f43-a36a-43742cb46bfe",
      "comment": "",
      "command": "click",
      "target": "name=registration_submit",
      "targets": [
        ["name=registration_submit", "name"],
        ["css=#register_form > .btn", "css:finder"],
        ["xpath=//button[@name='registration_submit']", "xpath:attributes"],
        ["xpath=//form[@id='register_form']/button", "xpath:idRelative"],
        ["xpath=//div[2]/form/button", "xpath:position"],
        ["xpath=//button[contains(.,'Зарегистрироваться')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "bb69f200-eba4-46e8-8708-bfa3bd7e07cb",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": []
  }],
  "urls": ["http://selenium1py.pythonanywhere.com/"],
  "plugins": []
}