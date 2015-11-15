#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cercles` module

:author: Sauvage Célestine ,Danneels Sophie , Soltysiak Samuel

:date: November-December, 2015

Module for cercle.


"""
import math

def create(x,y,r):
    """
    create a circle with center x which is  x-axis  and y-axis and r radius

    :param x: x-axis for the center of circle
    :type x: int or float
    :param y: y-axis for the center of circle
    :type y: int or float
    :param r: radius of  circle
    :type r: int or float
    :return: {'center':(x,y),'radius':r}
    :rtype: a dict
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> get_center(cercle)
    (250,250)
    >>> imag_part (z)
    2
    """
    return {'center':(x,y),'radius':r}

def get_center(cercle):
    """
    return the center (x-axis,y-axis)

    :param cercle: a circle
    :type z: a circle ( dict)
    :return: the center  of circle
    :rtype:tuple
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> get_center(cercle)
    (250,250)
    
    """
    return cercle['center']

def get_x_axis(cercle):
    """
    return x-axis
    
    :param cercle: a circle
    :type z: a circle ( dict)
    :return: x-axis of center of circle
    :rtype:float or int
    :UC: none
    :Example:
    >>> cercle = create(250,250,100)
    >>> get_x_axis(cercle)
    250
    """
    return get_center(cercle)[0]

def get_y_axis(cercle):
    """
    return y-axis
    
    :param cercle: a circle
    :type z: a circle ( dict)
    :return: y-axis of center of circle
    :rtype: float or int
    :UC: none
    :Example:
    >>> cercle = create(250,250,100)
    >>> get_y_axis(cercle)
    250
    """
    return get_center(cercle)[1]

def get_radius(cercle):
    """
    return the radius of center

    :param cercle: a circle
    :type z: a circle ( dict)
    :return: the raidus  of circle
    :rtype: int or float
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> get_radius(cercle)
    100
    
    """
    return cercle['radius']

from tkinter import *
fenetre=Tk()
can = Canvas(fenetre,bg='white',height=500,width=500)
can.pack()

def draw_circle(cercle):
    x=get_x_axis(cercle)
    y=get_y_axis(cercle)
    r=get_radius(cercle)
    can.create_oval(x-r, y-r, x+r, y+r) 

def r(cercle):
    return ((get_radius(cercle))*((1-math.sin(math.pi/3))/(1+(math.sin((math.pi/3))))))

def r1(cercle):
    return ((get_radius(cercle)*math.sin(math.pi/3))/(1+(math.sin((math.pi/3)))))

def alpha(i):
    """
    teste documentation
    """
    return (2*i*math.pi)/3

def cerclenimporte(r,r1,alpha,x,y):
    return (x+(r+r1)*math.cos(alpha),(r+r1)*math.sin(alpha)+y)

def quifaittout(cercle,n):
    draw_circle(cercle)
    r = r(cercle)
    r1 = r1(cercle)
    for i=1 in range (n+1):
        alpha= alpha(i)
        new_center=cerclenimporte(r,r1,alpha,get_x_axis(cercle),get_y_axis(cercle))
        create(new_center,r)

