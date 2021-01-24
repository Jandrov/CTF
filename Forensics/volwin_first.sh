#!/bin/bash
# Automatizador de Volatility para dumps de Windows

PLUGINS_DIR=/home/Documentos/plugins_volatility
OUTPUT_DIR=./volwin-first-out
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

# Comprobacion con pstree
ejecuta_comandos pstree

echo "[*] Comprobación de salida correcta de pstree:"
head $OUTPUT_DIR/pstree.txt

# Genericos
ejecuta_comandos psxview netscan cmdline cmdscan consoles hashdump mimikatz envars clipboard mftparser hivelist



