import subprocess

#################
#
# CONSTANTS
#
#################

camera_path = "/run/user/1000/gvfs/gphoto2:host=Canon_Inc._Canon_Digital_Camera/"
picture_folder = 'DCIM/101CANON/'
dash = ( '_', '-' )

#################
#
# FUNCTIONS
#
#################

def command( *commands, **kwcommands ) :

    command_line = []

    for command in commands :
        command_line += [ '--' + command ]
    
    for key, value in kwcommands.items() :
        command_line += [ '--' + key.replace(*dash) + '=' + str( value ) ]
    
    return command_line

    
def set_config_command( **configuration ) :
    
    command_line = []
    
    for key, value in configuration.items() :
        
        command_line += [ '--set-config',  key.replace(*dash) + '=' + str( value ) ]
    
    return command_line


def gphoto( command_line ) :
    return subprocess.run( [ "gphoto2" ] + command_line , capture_output = True )


def set_config( **configuration ) :
    return gphoto( set_config_command( **configuration ) )


def record_movie( duration = '5s', download = True ) :
    
    command_line = set_config_command( viewfinder = 1 )
    command_line += command( wait_event = '3s' )
    command_line += set_config_command( movierecordtarget = 0 )
    command_line += command( wait_event = duration )
    
    if download :
        command_line += set_config_command( movierecordtarget = 1 )
        command_line += command( wait_event_and_download = '2s' )
    
    return gphoto( command_line )


def ls( folder = picture_folder ) :
    
    output = subprocess.run( [ "ls", camera_path + folder ], capture_output = True )
    
    return output.stdout.decode().split('\n')[:-1]


def umount() :
    return subprocess.run( [ 'gio', 'mount', '-s', 'gphoto2' ], capture_output = True )


#################
#
# TRY IT OUT
#
#################


if __name__ == '__main__' :
        
    # ~ print( ls() )

    print( umount().stdout.decode() )
    
    print( set_config( capturetarget = 1 ).stdout.decode() )

    print( record_movie( duration = '2s' ).stdout.decode() )
