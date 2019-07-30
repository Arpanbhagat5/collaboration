import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        ParkingLot chiba = new ParkingLot();
		AdminUser adm = new AdminUser();
        // User arrived
        VehicleUser vUser1 = new VehicleUser();
		Vehicle vehicle1 = new Vehicle();

        //vUser1.getData();

        // Check availability
        //chiba.isAvailable();

        // Genrate token
        Token token1 = new Token();
        //System.out.println("New Token generated: " + token1.tokenNumber + " at " + token1.entryDate) ;

        // Slot assignment
        //System.out.println(vUser1.name + ", go to slot " + ParkingLot.takenSlots);
        //Thread.sleep(5000);

        // Exit
        //token1.duration = token1.calculateDuration();
        //System.out.println(vUser1.name + ", Please pay INR: " + token1.calculateCharge(token1.duration));
		
		// Show vehicle info for user
		//vehicle1.showVehicleInfo(vUser1);
		
		// Add vehicle user as a member
		//adm.makeMember(vUser1);
		
		/*Select option:
		1. Save User Data
		2. Show User Data
		3. Show Vehicle Information
		4. Check Parking Availability
		5. Show Token number
		6. Show Parked Vehicle Slot Number
		7. Calculate Parking Fare
		8. Apply for Membership
		9. Exit Menu
		*/
		Scanner scan = new Scanner(System.in);
		int input;
			
		do
		{
			System.out.println("1. Save User Data\n2. Show User Data\n3. Show Vehicle Information\n4. Check Parking Availability\n5. Show Token number\n6. Show Parked Vehicle Slot Number\n7. Calculate Parking Fare\n8. Apply for Membership\n9. Exit Menu");
			System.out.println("Please enter an option to proceed: ");
			input = scan.nextInt();
			switch(input) {
			case 1: System.out.println("Please Enter User data: ");
					System.out.println("Name: ");
					String name = scan.next();
					System.out.println("Contact Number: ");
					String contact = scan.next();
					System.out.println("User Type(e.g.vehicleUser): ");
					String userType = scan.next();
					System.out.println("Vehicle Number: ");
					String vehicleNumber = scan.next();
					System.out.println("Member ID(NA if not a member yet): ");
					String memberId = scan.next();
					vUser1.setData(name, contact, userType, vehicleNumber, memberId);
					System.out.println("User data saved successfully.");
					//vUser1.setData("Ayu", "987654321", "vehicleUser", "tok32", "NA");
					break;
			case 2: vUser1.getData();
					break;
			case 3: vehicle1.showVehicleInfo(vUser1);
					break;
			case 4: chiba.isAvailable();
					break;
			case 5: Token token1 = new Token();
					System.out.println("New Token generated: " + token1.tokenNumber + " at " + token1.entryDate) ;
					break;
			case 6: System.out.println(vUser1.name + ", Your vehicle is parked at slot no. " + ParkingLot.takenSlots);
					break;
			case 7: token1.duration = token1.calculateDuration();
					System.out.println(vUser1.name + ", Please pay INR: " + token1.calculateCharge(token1.duration));
					break;
			case 8: adm.makeMember(vUser1);
					break;
			case 9: System.out.println("*** THANK YOU ***");
					break;
			}
		} while(input != 9);		
        
    }
}