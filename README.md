# Interaccion ROS Package

UC3M Robot Operating Systems - Final Project

## Full system launch (local)

Full nodes system deployment with this roslaunch

```
roslaunch interaccion interaccion.launch
```

## Full system launch (local and remote)

Server nodes launch

```
roslaunch interaccion interaccion_rpi.launch
```

Local nodes launch

```
roslaunch interaccion interaccion_local.launch
```

## Extra: robot system navigation initialization

After launching multi-robot system from [robotics package](https://github.com/ramajoballester/robotics) with ```roslaunch robotics autonomous_multi_house.launch```, the system can be initialized by checking user data with

```
roslaunch interaccion robots_check.launch
```
