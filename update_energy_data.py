import datetime
import requests


def get_time(days):
  a = str(datetime.date.today() - datetime.timedelta(days=days))
  return a


def write_content(content, filename):
  with open(filename, 'w') as f:
    f.write(content)

def read_content(filename):
  with open(filename, "r") as f:
    return f.read()


def get_cookie():
  url = "https://joint-solution.digitalplatform.campus.com/service/WebFrame/0.1.0/login"
  s = requests.session()
  body = {
    "loginAccount": "Hibmtech",
    "password": "gz633kP#a@4",
    "verifyCode": ""
  }
  header = {"Content-Type": "application/json"}
  r = s.post(url=url, json=body, headers=header, verify=False)
  c = r.cookies
  Cookie_list = []
  for i in c:
    Cookie_list.append(i.name+"="+i.value)
  Cookie = ";".join(Cookie_list)
  # print(Cookie)
  Cookie_file = "Cookie.txt"
  write_content(Cookie, Cookie_file)


def get_csrftoken():
  url = "https://joint-solution.digitalplatform.campus.com/service/WebFrame/0.1.0/csrftoken"
  s = requests.session()
  Cookie = read_content("Cookie.txt")
  header = {"Cookie": Cookie, "Content-Type": "application/json"}
  body = {
  "httpMethod": "POST"
}
  r = s.post(url=url, headers=header, json=body, verify=False)
  return r.json()

def run_script(Cookie, csrftoken, script):
  url = "https://joint-solution.digitalplatform.campus.com/service/datatool_005/data-batch/v1/scripts/run"
  data = {
  "runId": "fe629d22-1ca8-44f9-a950-4c59caafa2ee",
  "content": script,
  "connectionName": "do_data_warehouse",
  "database": "dogaussdb_hibmtech",
  "scriptArgs": []
}
  header = {"Content-Type": "application/json", "Cookie": Cookie, "Csrf-Token": csrftoken}
  s = requests.session()
  r = s.post(url=url, json=data, headers=header, verify=False)
  print(r.json())


if __name__ == '__main__':
  get_cookie()
  Cookie = read_content("Cookie.txt")
  csrftoken = get_csrftoken()["result"]['csrfToken']
  yesterday = get_time(1)
  today = str(datetime.date.today())
  script = "UPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+today+" 12' WHERE log_hour = '"+yesterday+" 12';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+today+" 7' WHERE log_hour = '"+yesterday+" 7';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+today+" 8' WHERE log_hour = '"+yesterday+" 8';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+today+" 9' WHERE log_hour = '"+yesterday+" 9';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+today+" 10' WHERE log_hour = '"+yesterday+" 10';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+today+" 11' WHERE log_hour = '"+yesterday+" 11';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+get_time(24)+" 11' WHERE log_hour = '"+get_time(25)+" 11';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+get_time(24)+" 09' WHERE log_hour = '"+get_time(25)+" 09';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+get_time(21)+" 16' WHERE log_hour = '"+get_time(22)+" 16';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+get_time(19)+" 16' WHERE log_hour = '"+get_time(20)+" 16';\nUPDATE dwr_res.dws_res_park_h_f SET log_hour = '"+get_time(19)+" 09' WHERE log_hour = '"+get_time(20)+" 09';"
  # write_content(script, "script.txt")
  # print(script)
  run_script(Cookie, csrftoken, script=script)
