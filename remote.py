import sys
import os

def main():
    print os.name

#system values in order of CPU , RAM, Storage, Network
system_values = []

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'deploy':
            import paramiko

            # Connect to remote host
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect('192.168.56.102', username='anurag', password='anurag')

            # Setup sftp connection and transmit this script
            #sftp = client.open_sftp()
            #sftp.put(__file__, '/tmp/CPU.py')
            #sftp.close()

            # Run the transmitted script remotely without args and show its output.
            # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
            stdout = client.exec_command('python /home/anurag/cpu.py')[1]
            for line in stdout:
                # Process each line in the remote output
                system_values.append(line)

            client.close()
            print(system_values)
	    sys.exit(0)
	     
    except IndexError:
        pass

    # No cmd-line args provided, run script normally
    main()
