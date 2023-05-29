---------------

[Github link](https://github.com/diego-treitos/linux-smart-enumeration)

-----------------------

This shell script will show relevant information about the security of the local Linux system, helping to escalate privileges.

From version **2.0** it is _mostly_ **POSIX** compliant and tested with `shellcheck` and `posh`.

It can also **monitor processes to discover recurrent program executions**. It monitors while it is executing all the other tests so you save some time. By default it monitors during 1 minute but you can choose the watch time with the `-p` parameter.

It has 3 levels of verbosity so you can control how much information you see.

In the default level you should see the highly important security flaws in the system. The level `1` (`./lse.sh -l1`) shows interesting information that should help you to privesc. The level `2` (`./lse.sh -l2`) will just dump all the information it gathers about the system.

---------------------

Run ./lse.sh 