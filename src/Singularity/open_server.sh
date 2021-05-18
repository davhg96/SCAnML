token=$(cat logs/SC_arches_train$1.err | grep http | head -1 | cut -d' ' -f5)
firefox $token
