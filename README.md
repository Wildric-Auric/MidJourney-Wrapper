# MidJourney-Wrapper

## Presentation
The point of this bot is using [MidJouney](https://www.midjourney.com/home/) from an account other than the account you paid from.
To do so, there should be a Discord bot, which we will call DaVinci (see [Globals](https://github.com/Wildric-Auric/MidJourney-Wrapper/blob/main/Globals.py)), and the account subscribed to MidJourney, which we will call Salai, in the same server. Any discord user in the server can use DaVinci commands to generate images, their variations, upscale them...<br>
Warning though; you aren't allowed to use this software in the purpose of sharing your subscription with other people; this software is intended to be used only for learning purposes. If you infringe the rules, please know that you are solely responsible.

## Installation
* Clone the project.
* Install [requirements](https://github.com/Wildric-Auric/MidJourney-Wrapper/blob/main/requirements.txt) (only pycord version 2)  and discord python api module if needed. 
* Fill [Globals.py](https://github.com/Wildric-Auric/MidJourney-Wrapper/blob/main/Globals.py) with your data
* Run main.py;

## Implemented commands documentation
*MT stands for mandatory*
*OPT stands for optional*
### Generating idea
```
/mj_imagine [ MT : prompt (string)]
```


![ezgif-3-c4476f9a09](https://user-images.githubusercontent.com/70033490/185647413-1177b21a-2c2f-4f02-885e-c35d82179ba3.gif)


### Targetting image
Reply to MidJourney Bot message by the following command to target that piece of art for the next operation:
```
$mj_target
```
Notice that slash command is not used here because of discord not allowing Interactions during reply. Hence, there is no autocomplete, your reply is simply parsed to get the command.<br>


![ezgif-3-c4476f9a09](https://user-images.githubusercontent.com/70033490/185650795-06de185a-56ad-4c10-ac1d-34c5ca75b642.gif)


### Upscaling and variations
```
/mj_upscale [ MT : index (integer) ] [ OPT : reset_target (boolean) ]
```
*index* parameter takes values from 1 to 4; 1 is the index of top left image and 4 is the index of buttom right one.
The optional parameter *reset_target* indicates if target you have set before should be reset at the end of current operation; if that's done and you want to upscale image from same message with different index you should use *$mj_target* command again.


![ezgif-3-c4476f9a09](https://user-images.githubusercontent.com/70033490/185656154-ce31e7ba-29c9-4399-8086-5c7a4861ec26.gif)


Generated image:

![image](https://user-images.githubusercontent.com/70033490/185656359-895dbc6a-a0aa-47ff-a524-58a00b7edaa7.png)

Notice that we cannot use ```/mj_upscale_to_max``` on this output since we used *--hd* parameter which makes a sigle upscale maximized.<br>
This last command does not require a parameter and it resets target since no other operation is possible on this output other than upscaling to max. But remember that you need again to target what you need to upscale for the second time.<br>

There is another command that uses the output of ```/mj_imagine```:
```
/mj_upscale_to_max [ MT : index (integer) ] [ OPT : reset_target (boolean) ]
```
It behaves the same way as upscaling command.

## Additional information
Even though a request error is caught by the bot (a problem with MidJourney bot, a problem with the subscripted account...) since it shows up as HTTP request error, it does not caught errors done by the user; for example if there was a typo using MidJourney parameters like ```-hd``` instead of ```--hd``` MidJourney reports it to the subscripted user but DaVinci does not complain about it, so pay attention to your inputs. Also read the official user [documentation](https://midjourney.gitbook.io/docs/user-manual) of MidJourney.

*Enjoy!*



