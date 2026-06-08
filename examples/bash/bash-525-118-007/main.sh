slow_calculation() {
    local x=$1
    local y=$2
    local result
    
    # Длительная операция
    sleep 1
    
    result=$((x * y))
    echo "$result"
}

start_time=$(date +%s.%N)
for i in {1..10}; do
    slow_calculation 10 20
done
end_time=$(date +%s.%N)

echo "Время выполнения: $(echo "$end_time - $start_time" | bc)"
