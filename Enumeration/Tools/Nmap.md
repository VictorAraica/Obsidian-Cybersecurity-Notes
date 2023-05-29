------------

Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses.

-----------

## Port Specification options

Specific port
```nmap
nmap –p 23 172.16.1.1
```

Port range
```nmap
nmap –p 23-100 172.16.1.1
```

U-UDP,T-TCP different port types scan
```nmap
nmap -pU:110,T:23-25,443 172.16.1.1
```

All ports
```nmap
nmap -p- 172.16.1.1
```

Port scan from specified protocols
```nmap
nmap -smtp,https 172.16.1.1
```

Top ports
```nmap
nmap --top-ports 500 172.16.1.1
```

---------------------

## Verbose

```nmap
nmap 172.16.1.1 -v
```

---------------------

## DNS Resolution

Don't apply DNS Resolution
```
nmap 172.16.1.1 -n
```

---------------------

## Speed of the scan

T <paranoid | sneaky | polite | normal | aggressive | insane> (Set a timing template) Nmap offers a simple approach, with six timing templates. You can specify them with the -T option and their number (0–5) or their name. The template names are paranoid (0), sneaky (1), polite (2), normal (3), aggressive (4), and insane (5). The first two are for IDS evasion. Polite mode slows down the scan to use less bandwidth and target machine resources. Normal mode is the default and so -T3 does nothing. Aggressive mode speeds scans up by making the assumption that you are on a reasonably fast and reliable network. Finally insane mode assumes that you are on an extraordinarily fast network or are willing to sacrifice some accuracy for speed.

```nmap
nmap -T5 172.16.1.1 
```

---------------------

## Remove host discovery from scan

Treat all hosts as online -- skip host discovery
```nmap
nmap 172.16.1.1 -Pn
```

---------------------

## UDP Scan

```nmap
nmap -sU  172.16.1.1
```

-----------------

## Find open hosts

```nmap
nmap -sn 172.16.1.0/24
```

-------------------

## Os detection (not recommended)

```nmap
nmap -O 172.16.1.1
```

--------------------

## Service and version detection

```nmap
nmap -sV 172.16.1.1
```