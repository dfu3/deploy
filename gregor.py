from flask_api import FlaskAPI
import os

app = FlaskAPI(__name__)
backIP = '10.200.45.42'
frontIP = '10.200.45.31'

@app.route('/request/<string:mach>/<string:vers>')
def request(mach, vers):
	ret = {'mach' : mach, 'vers' : vers }

	deploy(mach, vers)
	
	return "SUCCESS"

def depBundle(mach, vers):

	myDB = MySQLdb.connect(host="localhost",port=3306,user="deploy",passwd="letMe1n",db="user_info")
	curs = myDB.cursor()
	bundLoc = curs.execute("select bundle_name from bundles where target='" + mach + "' and version_num='" + vers + "' ;")
	myDB.commit()
	
	if(mach == 'back'):
		os.system('scp ' + bundLoc + ' paul@' + backIP + ':/home/osru/bundles/')
		cmd = ['sshpass', '-p', 'dfu1357531', 'ssh', 'osru@' + backIP, 'python', 'install.py']

	elif(mach == 'front'):
		os.system('scp ' + bundLoc + ' manvi@' + frontIP + ':/home/manvi/bundles/')
		cmd = ['sshpass', '-p', 'manviPsswd', 'ssh', 'manvi@' + frontIP, 'python', 'install.py']


	#unzip
	ssh = subprocess.Popen(cmd, stdout=subprocess.PIPE)

if(__name__ == '__main__'):
	app.run(host='0.0.0.0', port=5000)