import argparse
import subprocess
import re
import os

def print_banner():
    banner = r"""
                                 )                   
 (          )              )  ( /(                )  
 )\ )    ( /(           ( /(  )\())    )       ( /(  
(()/(    )\())  (   (   )\())((_)\u00a0 ( /(   (   )\()) 
 /(_))_ ((_)   )\  )\ (_))/  _((_) )(_))  )\ ((_)  
(_)) __|| |(_) ((_)((_)| |_  | || |((_)_  ((_)| |_(_) 
  | (_ || ' \ / _ \(_-<|  _| | __ |/ _` |/ _| | / /  
   \___||_||_|\___//__/ \__| |_||_|\__,_|\__| |_\_\  
                                                   
             By erosennin420
    """
    print(banner)

def run_nmap_phase1(target):
    print("[+] Ejecutando Fase 1: Escaneo de puertos...")
    phase1_cmd = ["nmap", "-Pn", "-sS", "-T4", "-p-", "--min-rate", "1000", "--open", target]
    result = subprocess.run(phase1_cmd, capture_output=True, text=True)
    print(result.stdout)

    open_ports = re.findall(r"([0-9]+)/tcp\s+open", result.stdout)
    return ",".join(open_ports)

def run_nmap_phase2(target, ports):
    if not ports:
        print("[-] No se encontraron puertos abiertos. Abortando Fase 2.")
        return

    print("[+] Ejecutando Fase 2: Detección de servicios y SO...")
    phase2_cmd = ["nmap", "-sCV", "-p", ports, target]
    result = subprocess.run(phase2_cmd, capture_output=True, text=True)
    print(result.stdout)

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="GhostMap - Recon Tool por erosennin420")
    parser.add_argument("target", help="IP o dominio del objetivo")
    args = parser.parse_args()

    ports = run_nmap_phase1(args.target)
    run_nmap_phase2(args.target, ports)

if __name__ == "__main__":
    main()
