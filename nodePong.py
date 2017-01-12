import bpy


def gameWon():
    
    nodes = bpy.context.scene.node_tree.nodes
    playerScore = nodes['playerScore']
        
    return int(playerScore.label) == 3



def gameOver():
    
    nodes = bpy.context.scene.node_tree.nodes
    AIScore = nodes['AIScore']
        
    return int(AIScore.label) == 3



def showWon():
    
    nodeEditor = bpy.context.area.regions[3]
    width = nodeEditor.width
    height = nodeEditor.height   
    nodes = bpy.context.scene.node_tree.nodes
    wonText = "\nHooray, you won! Have another go? \n\nEsc - Quit the game \n\nSpace - Start a new game"
    wonNode = nodes.new("NodeFrame")
    x, y = nodeEditor.view2d.region_to_view(width/2, height/2)
    wonNode.width = 600
    wonNode.height = 270
    wonNode.location[0] = x - (wonNode.width/2)
    wonNode.location[1] = y + (wonNode.height/2)
    wonNode.label = "You Won!"
    wonNode.name = "won"
    wonNode.use_custom_color = True
    wonNode.color = (1, 1, 1)
    wonTextBlock = bpy.data.texts.new("wonTextBlock")
    wonTextBlock.write(wonText)
    wonNode.text = wonTextBlock



def showGameOver():
    
    nodeEditor = bpy.context.area.regions[3]
    width = nodeEditor.width
    height = nodeEditor.height   
    nodes = bpy.context.scene.node_tree.nodes    
    gameOverText = "\nWell, you mucked that one up. Have another go? \n\nEsc - Quit the game \n\nSpace - Start a new game"
    gameOverNode = nodes.new("NodeFrame")
    x, y = nodeEditor.view2d.region_to_view(width/2, height/2)
    gameOverNode.width = 600
    gameOverNode.height = 270
    gameOverNode.location[0] = x - (gameOverNode.width/2)
    gameOverNode.location[1] = y + (gameOverNode.height/2)
    gameOverNode.label = "Game Over"
    gameOverNode.name = "gameOver"
    gameOverNode.use_custom_color = True
    gameOverNode.color = (1, 1, 1)
    gameOverTextBlock = bpy.data.texts.new("gameOverTextBlock")
    gameOverTextBlock.write(gameOverText)
    gameOverNode.text = gameOverTextBlock



def moveBall(x, y):
    
    ballNodes = ["ballTop", "ballTop2", "ballRight", "ballBottom", "ballBottom2", "ballLeft", "ballEnd"]
    nodes = bpy.context.scene.node_tree.nodes
    
    for nodeName in ballNodes:
        
        nodes[nodeName].location[0] += x
        nodes[nodeName].location[1] += y
    


def setupGame(self):
        
    bpy.context.area.type = "NODE_EDITOR"
    bpy.context.area.spaces[0].tree_type = "CompositorNodeTree"
    bpy.context.scene.use_nodes = True
    
    bpy.ops.view2d.reset()
    nodeEditor = bpy.context.area.regions[3]
    width = nodeEditor.width
    height = nodeEditor.height   
     
    nodes = bpy.context.scene.node_tree.nodes    

    #Clear any existing nodes
    nodes.clear()    


    #Instructions     
    instructionsText = "\nUse the up and down arrows to control the paddle on the left \n\nEsc - Quit the game \n\nSpace - Start the game"
    instructionsNode = nodes.new("NodeFrame")
    x, y = nodeEditor.view2d.region_to_view(width/2, height/2)
    instructionsNode.width = 600
    instructionsNode.height = 270
    instructionsNode.location[0] = x - (instructionsNode.width/2)
    instructionsNode.location[1] = y + (instructionsNode.height/2)
    instructionsNode.label = "Instructions"
    instructionsNode.name = "instructions"
    instructionsNode.use_custom_color = True
    instructionsNode.color = (1, 1, 1)
    instructionsTextBlock = bpy.data.texts.new("instructionsTextBlock")
    instructionsTextBlock.write(instructionsText)
    instructionsNode.text = instructionsTextBlock


    #Bottom margin
    x, y = nodeEditor.view2d.region_to_view(0, 0)
    margin = nodes.new("NodeFrame")
    margin.location[0] = x
    margin.location[1] = y
    margin.name = "marginBottom"
    margin.label = " "


    #Paddles
    player = nodes.new("CompositorNodeRLayers")
    player.name = "Player"
    player.width = 100
    player.use_custom_color = True
    player.color = (0.911, 1, 1)
    AI = nodes.new("CompositorNodeRLayers")
    AI.name = "AI"
    AI.width = 100
    AI.use_custom_color = True
    AI.color = (0.911, 1, 1)
    

    #Paddle locations     
    x, y = nodeEditor.view2d.region_to_view(0, height/2)
    player.location[0] = x + 10
    player.location[1] = y + (player.height/2)
    x, y = nodeEditor.view2d.region_to_view(width, height/2)
    AI.location[0] = x - AI.width - 30
    AI.location[1] = y + (AI.height/2)


    #Score nodes
    x, y = nodeEditor.view2d.region_to_view(width/2, height)
    
    #Player node
    scoreNode = nodes.new("NodeFrame")
    scoreNode.location[1] = y - 10
    scoreNode.use_custom_color = True            
    scoreNode.width = 132
    scoreNode.height = 55
    scoreNode.name = "playerScore"
    scoreNode.location[0] = x - 142
    scoreNode.color = (0, 1, 0)  
    scoreNode.label = "0"
    scoreNode.label_size = 64
    
    #AI node
    scoreNode = nodes.new("NodeFrame")
    scoreNode.location[1] = y - 10
    scoreNode.use_custom_color = True            
    scoreNode.width = 132
    scoreNode.height = 55
    scoreNode.name = "AIScore"
    scoreNode.location[0] = x + 10
    scoreNode.color = (1, 0, 0)  
    scoreNode.label = "0"
    scoreNode.label_size = 64
    
    for j in range(0, 2):        

        for i in range(1, 4):

            scoreNode = nodes.new("NodeFrame")
            scoreNode.location[1] = y - 10
            scoreNode.use_custom_color = True            
            scoreNode.width = 132                
            scoreNode.label = " "
            scoreNode.height = 30
            
            #Player nodes    
            if j == 0:
                
                scoreNode.name = "playerScore"+str(4 - i)
                scoreNode.location[0] = x - (142 * i) - 142
                scoreNode.color = (0, 1, 0)
            
            #AINodes
            else:
                
                scoreNode.name = "AIScore"+str(4 - i)
                scoreNode.location[0] = x + (142 * i) + 10
                scoreNode.color = (1, 0, 0)
                
            
    for node in nodes:
        node.select = False        



def endGame(self):
    
    bpy.context.scene.node_tree.nodes.clear()
    texts = bpy.data.texts
    
    if self.messageBoxTextBlock in bpy.data.texts:    
        bpy.data.texts.remove(bpy.data.texts[self.messageBoxTextBlock], do_unlink=True)
         
    bpy.context.area.type = "TEXT_EDITOR"



def updateScore(playerScoreName, opponentScoreName):
    
    nodes = bpy.context.scene.node_tree.nodes
    playerScore = nodes[playerScoreName]
    
    playerScore.label = str(int(playerScore.label) + 1)
    score = playerScore.label
    nodes[opponentScoreName+score].color = (1, 1, 1)



def paddleAtBoundary(paddleName, side):
    
    nodeEditor = bpy.context.area.regions[3]
    height = nodeEditor.height        
 
    x, y = nodeEditor.view2d.region_to_view(0, height)

    nodes = bpy.context.scene.node_tree.nodes
    paddle = nodes[paddleName]
        
    if side == "top":
        
        return paddle.location[1] >= y - 20
        
    elif side == "bottom":
        
        return paddle.location[1] <= -y + paddle.height# + 275



def ballAtBoundary(side):
        
    nodes = bpy.context.scene.node_tree.nodes
    
    if side == "right":
        
        return nodes['ballRight'].location[0] >= nodes['AI'].location[0] + nodes['AI'].width
    
    elif side == "left":
        
        return nodes['ballLeft'].location[0] <= nodes['Player'].location[0]
    
    elif side == "bottom":
        
        return nodes['ballBottom'].location[1] <= nodes['marginBottom'].location[1] + 35
    
    elif side == "top":

        return nodes['ballTop'].location[1] >= nodes['playerScore'].location[1] - nodes["playerScore"].height - 20
        


def ballCollidingWithPaddle(direction):
    
    nodes = bpy.context.scene.node_tree.nodes
    
    playerX = nodes['Player'].location[0] + nodes['Player'].width
    playerY = nodes['Player'].location[1]
    AIX = nodes['AI'].location[0]
    AIY = nodes['AI'].location[1]
    
    if direction == "left":
        
        ballNodeNames = ['ballBottom2', 'ballLeft', 'ballTop']
        
        #x is aligned
        #Second comparison prevents ball being deflected when the ball is behind the paddle
        if nodes['ballLeft'].location[0] <= playerX and nodes['ballLeft'].location[0] > playerX - 10:
        
            for ballNodeName in ballNodeNames:
            
                ballNode = nodes[ballNodeName]
             
                #Check paddle's top margin
                if ballNode.location[1] <= playerY + 20:
                    
                    #Check paddle's bottom margin
                    if ballNode.location[1] >= playerY - 230:

                        return True
                    
                
    elif direction == "right":

        ballNodeNames = ['ballTop2', 'ballRight', 'ballBottom']
        
        if nodes['ballRight'].location[0] >= AIX and nodes['ballRight'].location[0] < AIX + 10:
                
            for ballNodeName in ballNodeNames:
                
                ballNode = nodes[ballNodeName]
                                            
                if ballNode.location[1] <= AIY + 20:
                    
                    if ballNode.location[1] >= AIY - 230:

                        return True
                                            
    return False
    


def newGame(self):
    
    nodes = bpy.context.scene.node_tree.nodes
    nodeEditor = bpy.context.area.regions[3]
    height = nodeEditor.height  
     
    playerScore = nodes['playerScore'].label = '0'
    AIScore = nodes['AIScore'].label = '0'
        
    nodes['AIScore1'].color = (1, 0, 0)
    nodes['AIScore2'].color = (1, 0, 0)
    nodes['AIScore3'].color = (1, 0, 0)
    nodes['playerScore1'].color = (0, 1, 0)
    nodes['playerScore2'].color = (0, 1, 0)
    nodes['playerScore3'].color = (0, 1, 0)  
    
    player = nodes['Player']
    AI = nodes['AI']
    x, y = nodeEditor.view2d.region_to_view(0, height/2)
    player.location[1] = y + (player.height/2)
    AI.location[1] = y + (AI.height/2) 
    
    bpy.data.texts.remove(bpy.data.texts[self.messageBoxTextBlock], do_unlink=True)
    nodes.remove(nodes[self.messageBoxNode])    
    
    addBall(self)
    


def addBall(self):
    
    nodes = bpy.context.scene.node_tree.nodes
    nodeEditor = bpy.context.area.regions[3]
    width = nodeEditor.width
    height = nodeEditor.height    
    nodeLinks = bpy.context.scene.node_tree.links

    ballNodeList = [["ballTop", -10, 17.5], 
                    ["ballTop2", 10, 17.5], 
                    ["ballRight", 20, 0], 
                    ["ballBottom", 10, -17.5], 
                    ["ballBottom2", -10, -17.5], 
                    ["ballLeft", -20, 0], 
                    ["ballEnd", -10, 17.5]]

    x, y = nodeEditor.view2d.region_to_view(width/2, height/2)

    previousNode = None
        
    for ballNodeName in ballNodeList:
                        
        ballNode = nodes.new("NodeReroute")
        ballNode.name = ballNodeName[0]
        ballNode.location[0] = x + ballNodeName[1]
        ballNode.location[1] = y + ballNodeName[2]
        
        if ballNodeName[0] != "ballTop":
            
            nodeLinks.new(ballNode.inputs[0], previousNode.outputs[0])
            
        ballNode.select = False
                
        previousNode = ballNode


    
def removeBall():

    nodes = bpy.context.scene.node_tree.nodes
    
    ballList = ["ballTop", "ballTop2", "ballRight", "ballBottom", "ballBottom2", "ballLeft", "ballEnd"]
    
    for ballNodeName in ballList:
        
        nodes.remove(nodes[ballNodeName])



def updateAI():
    
    nodeEditor = bpy.context.area.regions[3]
    height = nodeEditor.height        
 
    x, y = nodeEditor.view2d.region_to_view(0, height)
    
    nodes = bpy.context.scene.node_tree.nodes
    AI = nodes['AI']
    ballLeft = nodes['ballLeft']
    
    moveDistance = 5
        
    #'abs' to make sure distance is always positive, for later comparison    
    ballDistance = abs(AI.location[1] - (ballLeft.location[1] + 115))
    
    #Only move AI paddle if ball is not already very close - stops jittering
    if ballDistance > moveDistance:
    
        #Ball above AI
        if AI.location[1] < ballLeft.location[1] + 115 and not paddleAtBoundary("AI", "top"):
            
            AI.location[1] += moveDistance
        
        #Ball below AI   
        elif AI.location[1] > ballLeft.location[1] + 115 and not paddleAtBoundary("AI", "bottom"):
            
            AI.location[1] -= moveDistance



class Pong(bpy.types.Operator):
    """Play a classic game of Node Editor Pong™"""
    bl_idname = "node.pong"
    bl_label = "Start Pong!"
    
    ballSpeed = 8
    directionX = ballSpeed
    directionY = -ballSpeed
    paddleSpeed = 12
    timer = None
    paused = True
    messageBoxNode = "instructions"
    messageBoxTextBlock = "instructionsTextBlock"
    
    
    def modal(self, context, event):
        
        nodes = bpy.context.scene.node_tree.nodes
        playerScore = nodes['playerScore']
        AIScore = nodes['AIScore']
        
        if not self.paused:
                            
            if not gameOver() and not gameWon():
                                    
                if ballAtBoundary("right"):
                
                    self.directionX = -self.ballSpeed
                    updateScore('playerScore', 'AIScore')
                
                elif ballAtBoundary("left"):
                    
                    self.directionX = self.ballSpeed
                    updateScore('AIScore', 'playerScore')
                                        
                elif ballAtBoundary("bottom"):
                
                    self.directionY = self.ballSpeed
                    
                elif ballAtBoundary("top"):
                    
                    self.directionY = -self.ballSpeed
                    
                elif ballCollidingWithPaddle("left"):
                    
                    self.directionX = self.ballSpeed
                
                elif ballCollidingWithPaddle("right"):
                    
                    self.directionX = -self.ballSpeed
                
                moveBall(self.directionX, self.directionY)
                updateAI()
            
            elif gameOver():
            
                showGameOver()
                self.paused = True
                self.messageBoxNode = "gameOver"
                self.messageBoxTextBlock = "gameOverTextBlock"
                removeBall()
            
            elif gameWon():
                
                showWon()
                self.paused = True
                self.messageBoxNode = "won"
                self.messageBoxTextBlock = "wonTextBlock"
                removeBall()
        
        if event.type == "SPACE" and self.paused:
            
            self.paused = False
            newGame(self)
                                
        elif event.type == 'UP_ARROW' and not paddleAtBoundary("Player", "top") and not self.paused:
            
            nodes['Player'].location[1] += self.paddleSpeed 
            
        elif event.type == 'DOWN_ARROW' and not paddleAtBoundary("Player", "bottom") and not self.paused:

            nodes['Player'].location[1] -= self.paddleSpeed 

        elif event.type == 'ESC':
            
            endGame(self)
                        
            wm = context.window_manager
            wm.event_timer_remove(self.timer)
            
            return {'FINISHED'}

        return {'RUNNING_MODAL'}



    def invoke(self, context, event):
          
        setupGame(self)
     
        wm = context.window_manager
        self.timer = wm.event_timer_add(0.002, context.window)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
 


def register():
    bpy.utils.register_class(Pong)


def unregister():
    bpy.utils.unregister_class(Pong)


if __name__ == "__main__":
    register()
    
    bpy.ops.node.pong('INVOKE_DEFAULT')