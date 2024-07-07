A small script imitating the movie: "Who Am I - There is No Absolutely Safe System"

hacker_script_server.py: server

malicious program:

client_main.py: main program entry; just execute it directly

hacker_script.py: program main function: get ip and take photos of victims

email_send.py: send the photos taken to the attacker's mailbox by sending emails

Note: no additional program conditions are considered, just implement the function!

email_send.py file configures your own mailbox and authorization code

Principle: the victim executes the client_main.py file to get the victim's ip and call the victim's camera to take photos; the ip is transmitted to the attacker's server, and the server receives the ip and saves it as a file. The photos taken are saved as jpg pictures and sent to the attacker's mailbox via email


