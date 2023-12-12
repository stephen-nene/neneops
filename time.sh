watch -n1 "date '+%D%n%T'|figlet -k"
 while true; do echo "$(date '+%D %T' | toilet -f term -F border --gay)"; sleep 1; done
