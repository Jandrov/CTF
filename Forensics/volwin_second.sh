#!/bin/bash
# Automatizador de Volatility para dumps de Windows

PLUGINS_DIR=/home/Documentos/plugins_volatility
OUTPUT_DIR=./volwin-second-out
DUMP_DIR="$OUTPUT_DIR/dump"
DUMP=
PROFILE=

# Trap Ctrl+C
trap ctrl_c INT
function ctrl_c() {
    echo "Saliendo..."
}


if [ $# -lt 1 ]; then
	echo "[!] Uso: volwin <dump> [perfil-windows]"
	exit 1
fi

DUMP=$1
if [ ! -f "$1" ]; then
	echo "[!] No existe el archivo $DUMP. Comprueba la ruta."
	exit 1
fi

if [ $# -lt 2 ]; then
	# Detección de perfil automática
	echo "[*] Detectando perfil..."
	perfiles=$(volatility -f $DUMP imageinfo | grep -i profile | grep -v "No suggestion" | cut -d ':' -f2)

	if [ -z "$perfiles" ]; then
		echo "[!] No se pudo detectar el perfil del volcado."
		exit 1
	else
		echo "[*] Se han detectado los perfiles $perfiles"
		PROFILE=$(echo $perfiles | cut -d ',' -f1)
		echo "[*] Se utilizará el perfil $PROFILE."
	fi
else
	# Uso de perfil especificado
	PROFILE=$2
	echo "[*] Utilizando perfil $PROFILE."
fi


mkdir $OUTPUT_DIR 2>/dev/null
mkdir $DUMP_DIR 2>/dev/null

# Función que ejecuta los comandos que se le pasan como una lista por argumento
function ejecuta_comandos {
	while [ $# -gt 0 ]; do
		command=$1
		echo "[*]" $command
		volatility --plugins=$PLUGINS_DIR -f $DUMP --profile=$PROFILE $command > "$OUTPUT_DIR/$command.txt"
		shift
	done
}

# Genericos
ejecuta_comandos filescan

# Navegadores (mejorar detección)
ejecuta_comandos iehistory
if [ $(cat "$OUTPUT_DIR/filescan.txt" | grep -i "Firefox") -ne 0 ]; then
	echo "[*] Firefox detectado."
	ejecuta_comandos firefoxhistory firefoxcookies firefoxdownloads
fi

# TODO Mejorar deteccón. Ha matcheado otros archivos
if [ $(cat "$OUTPUT_DIR/filescan.txt" | grep -i "Chrome") -ne 0 ]; then
	echo "[*] Chrome detectado."
	ejecuta_comandos chromehistory chromevisits chromesearchterms chromedownloads chromedownloadchains chromecookies
fi

# TrueCrypt
if [ $(cat "$OUTPUT_DIR/filescan.txt" | grep -i "TrueCrypt") -ne 0 ]; then
	echo "[*] TrueCrypt detectado."
	ejecuta_comandos truecryptpassphrase truecryptsummary truecryptmaster
fi

# Malware
ejecuta_comandos malfind psscan

ejecuta_comandos sessions deskscan wndscan

# Misceláneo
#ejecuta_comandos shimcache shellbags sessions deskscan wndscan messagehooks wintree

# Persistencia (toma mucho tiempo)
#ejecuta_comandos autoruns

# Strings
strings $DUMP > "$OUTPUT_DIR/strings.txt"

