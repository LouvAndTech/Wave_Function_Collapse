from display import Screen
from compute import Map

def generate_a_map():
    world = Map()
    screen.printImage(world.map[world.coord[0]][world.coord[1]].imagePath,(world.coord[0],world.coord[1]))
    for i in range((40*23)-1):
        #for i in range(10):
        world.addTile()
        screen.printImage(world.map[world.coord[0]][world.coord[1]].imagePath,(world.coord[1]*32,world.coord[0]*32))
        screen.updateScreen()


if __name__ == "__main__":  
    
    """========== Screen initialisation =========="""

    print("Start screen...")
    screen = Screen()
    screen.fondDecran()
    screen.updateScreen()
    print("Screen up")

    """========== Handle map =========="""
    screen.eventGet()
    #Set a map
    generate_a_map()

    """========== Main Loop =========="""
    running = True
    while(running):
        # for loop through the event queue  
        for event in screen.eventGet():
            # Check for QUIT event      
            if event.type == screen.QUITEVENT:
                print("Quit event")
                running = False
            if event.type == screen.KEYDOWN:
                if event.key == screen.K_SPACE:
                    screen.fondDecran()
                    generate_a_map()

        screen.updateScreen()
            