class VehicleUser extends User {
    StringBuffer vehicleNumber;
    StringBuffer memberId;
    public void getData(VehicleUser user) {
        System.out.println("Vehicle User : "+ user.name);
        System.out.println("User ID : "+ user.memberId);
        System.out.println("User contact : "+ user.contact);
        System.out.println("USer vehicle number : "+ user.vehicleNumber);
    }
}