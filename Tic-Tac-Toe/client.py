# Python program to implement client side of chat room.
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))







def print_board(board):
    
    print "The board look like this: \n"
    
    for i in range(3):
        print " ",
        for j in range(3):
            if board[i*3+j] == 1:
                print 'X',
            elif board[i*3+j] == 0:
                print 'O',
            elif board[i*3+j] != -1:
                print board[i*3+j]-1,
            else:
                print ' ',
            
            if j != 2:
                print " | ",
        print
        
        if i != 2:
            print "-----------------"
        else:
            print


while True:
    
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
    
    """ There are two possible input situations. Either the
        user wants to give  manual input to send to other people,
        or the server is sending a message  to be printed on the
        screen. Select returns from sockets_list, the stream that
        is reader for input. So for example, if the server wants
        to send a message, then the if condition will hold true
        below.If the user wants to send a message, the else
        condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    
    board = []
    for i in range(9):
        board.append(-1)
    
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            message = int(message)
            if message >= 2 and message <= 10:
                print message
                print_board(message)
#print message
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
