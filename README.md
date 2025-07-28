# *XeyronoxDDOS (Free Version, v1.0)*

*XeyronoxDDOS for educational and basic features only.*

# *Overview*


*Tool Name: XeyronoxDDOS (Free Version, v1.0)*


*Developer: xeyronox (Red/Black Hat Hacker)*



*Contact: Instagram @xeyronox*



*Purpose: Network traffic simulator for educational CTF use*



*Version Note: This is a free version with basic features only. No upgrades available in the free version. For paid version (v1.2 or higher), contact @xeyronox on Instagram.*

# *Features*

bash '''
*CLI-based interface with three traffic modes:*



*Low: 1 request/sec, small payload (100B)*



*Medium: 5 requests/sec, medium payload (1KB)*



*High: 10 requests/sec, large payload (5KB)*



*30-minute runtime limit per session*



*Self-destruct mechanism: Script encrypts and corrupts itself after one run, deletes logs and tracking files*



*Random User-Agent headers for CTF rate-limiting bypass simulation*



*Temporary logging to traffic_sim.log (deleted on self-destruct)*



*Tracks last run time via last_run.txt (deleted on self-destruct)*
'''

# Requirements

*Python 3*

bash '''
*Dependencies: Install via pip install requests rich cryptography*
'''

*Compatible with Termux, Pydroid3, or other CLI environments*

# *Usage*


*Run the script: python XeyronoxDDOS_v1 0.py*



*Enter a CTF target URL when prompted (default: http://127.0.0.1:8080)*



*Select a traffic mode (1-3) or exit (4)*



*Script runs for up to 30 minutes or until stopped (Ctrl+C)*



*Self-destructs after completion, rendering the script unrecoverable*


# *Notes*


*For educational CTF use only*


*No upgrades available in free version (v1.0)*


*For paid version (v1.2+), contact Instagram @xeyronox*