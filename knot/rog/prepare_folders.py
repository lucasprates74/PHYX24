import os 

rate = 0.5
data = "C:/Users/prate/Desktop/Assignments/School/4thYr/2-Winter/PHY424/knot/rog/lp_rog_vids/"
code = "C:/Users/prate/Desktop/Assignments/School/4thYr/2-Winter/PHY424/knot/rog/knot-master/python/" 

for n in range(11,12):
    # os.system(f"ffmpeg -i {data}trial{n}.mp4 -filter:v \"crop=1400:880:100:200\" {data}trial{n}-crop.mp4")
    os.system(f"ffmpeg -i {data}trial{n}.mp4 -r {rate} {data}trial{n}/frame-%4d.png")
    os.system(f"python {code}process_rog.py --fileno=trial{n}")