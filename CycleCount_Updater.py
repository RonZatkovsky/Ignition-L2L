import requests
import time

def setCycleCount(apikey,machines):
    if(not machines):
        print("No active machines")
    else:
        for machine_pair in machines:
            try:
                if machine_pair[0]:        #for testing purposes, remove when ready to launch.
                    print(machine_pair[0])
                    url="https://edgewell.leading2lean.com/api/1.0/machines/set_cycle_count/"+"?auth="+apikey+"&site=800"+"&code="+machine_pair[0].replace(" ","%20")+"%20PM"+"&cyclecount="+str(machine_pair[1])
                    response=requests.post(url, verify=False)
                    # print(url)
                    if response.status_code == 200:
                        response_json = response.json()
                        if response_json['success']:
                            print(f"Cycle count updated successfully for {machine_pair[0]}.")
                            print(response_json)
                        else:
                            print("Failed to update cyclecount. Error message:", response_json.get('error'))
                    else:
                        print("Failed to update cyclecount. Status code:", response.status_code)
                        print("Response:", response.text)
            except requests.exceptions.RequestException as e:
                print("Error:", e)
                return None
   
def adjustNames(machines):
    try:
        for i in range(len(machines)):
            name, cyclecount = machines[i]
            if "-" in str(name):
                name = name.replace(" ", "")
            machines[i] = (name, cyclecount)
    except Exception as e:
        print("Error:", e)
        return None
        

def get_dispatches():
    machine_arr=[]
    url = "https://usmilignp01.care.corp:8043/system/ws/rest/to_l2l_Production_Cycle"
    # print(url)
    try:
        resp = requests.get(url, verify=False)  # Disable SSL verification
        resp.raise_for_status()
        
        data = resp.json()
        for item in data['content']:
            if (data['content'][item]['status']=="true" or data['content'][item]['status']=="1") and data['content'][item]['cyclecount']!=None:
                machine_arr.append((" ".join(item.split()[0:2]),data['content'][item]['cyclecount']))
    
        return machine_arr 
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    
api="VgV2wRAIaFfjqJxvndeafde4H5Prq0Hx"

while True:
    machines=get_dispatches()
    adjustNames(machines)
    print(machines)
    setCycleCount(api,machines)
    time.sleep(3600)

    # 90 parts per minute #*3 lanes, 270
