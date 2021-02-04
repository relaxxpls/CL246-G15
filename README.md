# OpenFOAM
Source Code for CL246 Project

**Installation Intructions**  

1. Go to [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and follow the *manual instruction* steps presented there.  

2. Check if you've succesfully installed WSL, and make sure your using WSL 2, i.e. `wsl -l -v`  on cmd should show:  
```  
  NAME      STATE           VERSION  
* Ubuntu    Running         2  
```  
or something similar, just that VERSION should be 2.  
*All instructions henceforth should be followed on the Linux (Ubuntu) terminal*

3. Install OpenFOAM 8:
```Shell
sudo sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
sudo add-apt-repository http://dl.openfoam.org/ubuntu
sudo apt-get update
sudo apt-get install openfoam8
```

4. User configuration (required *only once*):
- You need to setup commands for using OpenFOAM and ensure that the DISPLAY element is setup correctly.  
```Shell
echo ". /opt/openfoam8/etc/bashrc" >> $HOME/.bashrc
echo "export DISPLAY="$(/sbin/ip route | awk '/default/ { print $3 }'):0"" >> $HOME/.bashrc
echo "export LIBGL_ALWAYS_INDIRECT=1" >> $HOME/.bashrc
```

5. Source the bashrc file (*This step needs to be repeaated everytime you open a new terminal window!*):  
`source $HOME/.bashrc` can be used, or alternatively `. $HOME/.bashrc` would work.
Lazy? Update the terminal's startup file to include bashrc by default!
```Shell
echo "source "$HOME/.bashrc"" >> $HOME/.profile
```

6. Tired of the cascadia terminal life and want some GUI? Too Bad, WSL dosen't support that *yet*. 
An alternative is a Virtual Display ([Xming]() or 
Lazy? Create a [XLaunch Shortcut](https://siliconheaven.info/xlaunch-configuration-file/#gsc.tab=0)  
*Make sure that XLaunch is running and before calling the Linux GUI Apps on Windows Desktop environment.*
