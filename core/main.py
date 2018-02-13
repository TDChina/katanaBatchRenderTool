#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = "ZhaoTangjun"
# Email:252922079@qq.com


from Katana import NodegraphAPI
from Katana import KatanaFile
from Katana import RenderManager
from Katana import FarmAPI


def messageHandler( sequenceID, message ):
    print message

	
# main function
def kb_render(frame_range, file_path, resolution, camera, render_node): 

	renderSettings.asynchRenderMessageCB=messageHandler
	renderSettings.asynch=False
	
	frame_range = set_frame_range()
	file_path = set_file_path()
	resolution = set_resolution()
	camera = set_camera()
	render_node = set_render_node()
	
for frame in range(frame_range[0], frame_range[1]):
	print '-' * 80
	print '\nRendering Node "%s" frame %s...' % (set_rander_node().getName(), frame)
	renderSettings.frame = frame * time_increment # TODO frame < 1 则为1
	RenderManager.StartRender('diskRender', nodelist=set_rander_node(), settings=renderSettings)

	
# set frame range
def set_frame_range():
    # TODO 接受用户输入数值
    start_frame = NodegraphAPI.NodegraphGlobals.GetInTime()
    end_frame = NodegraphAPI.NodegraphGlobals.GetOutTime()
    time_increment = NodegraphAPI.NodegraphGlobals.GetTimeIncrement()
    return start_frame, end_frame, time_increment

	
# set filepath
def set_file_path():
	# TODO 接受用户输入数值
	path = NodegraphAPI.GetNode('RenderOutputDefine').getParameter('args.renderSettings.outputs.outputName.locationSettings.renderLocation.value').getValue(0)
		return path

		
# set resolution
def set_resolution():
	# TODO 接受用户输入数值
	res = NodegraphAPI.GetNode('rootNode').getParameter('resolution').getValue(0)
	# NodegraphAPI.GetNode('rootNode').getParameter('resolution').setValue("2000x2000",0)
	return res

	
# set camera
def set_camera():
	# TODO 接受用户输入数值
	cam = NodegraphAPI.GetNode('rootNode').getParameter('katanaSceneName').getValue(0)
	return cam
	
	
# set render node
def set_render_node():
	# TODO 接受用户输入数值
    node = NodegraphAPI.GetNode('Render1') # Render1 想做成用户直接拖拽渲染节点进来
	return node
