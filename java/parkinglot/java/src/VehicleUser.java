class VehicleUser extends User {
    String vehicleNumber;
    String memberId;
    public void setData(String name, String contact, String userType, String vehicleNumber, String memberID) {
        this.name = name;
        this.contact = contact;
        this.userType = userType;
        this.vehicleNumber = vehicleNumber;
        this.memberId = memberID;
    }
    public void getData() {
        System.out.println("Vehicle User : "+ this.name);
        System.out.println("User contact : "+ this.contact);
        System.out.println("User type : "+ this.userType);
        System.out.println("User vehicle number : "+ this.vehicleNumber);
        System.out.println("User ID : "+ this.memberId);

    }
}