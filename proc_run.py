import subprocess

p1=subprocess.Popen(['ping','google.com','-c','2']);
p2=subprocess.Popen(['sleep','3']);
p2.wait();
p1.kill();

