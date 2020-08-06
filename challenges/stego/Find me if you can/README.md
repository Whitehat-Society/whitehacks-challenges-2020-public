# Find me if you can :)

Author: haojun

Hiding information from plain sight (not the unintended version) and using that information to locate someone in the world.

# Description

I am having a catch up with my friends. Could you guess where am I?
https://ibb.co/3phJgkg

Submit the building name with the flag format.


# Solution

After downloading the image, you could perform some color channel edit. The coordinates will be shown after only having blue color channel.

or use tools like https://29a.ch/photo-forensics with principal component analysis (PCA) options to view coordinates clearly.

or you can just use exiftool to reveal the coordinates on the layer text.

After entering the coordinates onto google map. Click around the building, you will identify the building name.

You should end up having the building name in this format https://www.google.com.sg/maps/place/CJ+E%26M/@37.5784649,126.891294,19z/data=!4m5!3m4!1s0x357c99129258b129:0x5362c1d210f32957!8m2!3d37.5784979!4d126.8916963

There's no need to guess the building name actually, if you have properly identified the building name through google map.

# Flag

`WH2020{CJ E&M}`

