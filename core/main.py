import NodegraphAPI
from Katana import KatanaFile
from Katana import RenderManager
from Katana import FarmAPI

def messageHandler( sequenceID, message ):
    print message


RenderNode = NodegraphAPI.GetNode('Render1') # Getting Render node
renderSettings = RenderManager.RenderingSettings()
renderSettings.frame=1
renderSettings.mode=RenderManager.RenderModes.DISK_RENDER
renderSettings.asynchRenderMessageCB=messageHandler
renderSettings.asynch=False
FrameNum = FarmAPI.GetSceneFrameRange()
startFrame = FrameNum['start']
endFrame = FrameNum['end'] + 1

for frame in range(startFrame, endFrame):
    print '-' * 80
    print '\nRendering Node "%s" frame %s...' % (RenderNode.getName(), frame)
    renderSettings.frame = frame
    RenderManager.StartRender('diskRender', node=RenderNode, settings=renderSettings)