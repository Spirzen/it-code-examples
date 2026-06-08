# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204"
  config.vm.Сеть "private_network", ip: "192.168.56.10"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
    # Запрет выхода в интернет
    vb.customize ["modifyvm", :id, "--natpf1", "delete", "http"]
  end
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y strace ltrace binutils yara jq
  SHELL
end
