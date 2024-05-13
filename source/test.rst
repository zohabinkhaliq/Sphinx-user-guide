Testing
=======

Internet Facing ApplicationsIFA 

The Internet Facing application can be accessed by users or clients on
the Internet. For example, the IFA can be a web application an
enterprise can host in their VPC/VNET and allow access to the users on
the Internet which could comprise of their customers, partners or
employees.

To navigate to this section, select the internet-facing applications
icon
|https://lh7-us.googleusercontent.com/syFrus3YO7kSToMYupHc7njrFqW-mB17l0JgPUyo5fIIFFZfmya8MwV-VbYsNYbQu946zpTIPw1moBhmch6VMHMcDUZVk111pAb2iG2qJCYuzKbI16VF-hQbK2uxIV__moJ3BhIdbxtF1lHzQgKhVJs|
from the navigation sidebar to the left.

FAQs

What does the architecture for the Internet-facing applications look
like?

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image2.png
   :alt: https://lh7-us.googleusercontent.com/qSxxhe7obNOvJp2dnXLqAlVbE1JknbQkGDqWRzRG-BAO7BQBAl4_QCixMYvgKMAH9dc5cbQEP8RErxfyzg0lLu8RhEDlF512Yb8rUbSa4d6Dn4oCli_1GcWX7RiwaZ71Tc726yNjVvdn3VfAHZMns1M
   :width: 6.5in
   :height: 3.48958in

-  Internet-facing applications (IFA) are applications hosted in Alkira
   CXP serving users accessing and initiating the connections from the
   Internet

-  As a general rule Alkira CXP does not allow internet traffic in the
   ingress direction. IFA is an exception that allows applications to be
   served from the CXP

-  The value proposition of such applications for enterprises is that
   their workloads or applications like web servers that they want to
   host in the CXP and have them face the internet can be provisioned
   using a connector with minimal configuration effort and added
   features like firewall for security purposes. 

Which connectors can be used to provision internet-facing applications?

You can provision internet-facing applications using both on-prem or
cloud connectors.

What are the benefits of using the Internet-facing applications feature?

 

There are multiple benefits of using Alkira internet-facing applications
as described below:

-  When the Internet Facing applications are deployed, Alkira provides
   an FQDN for the application. 

-  Alkira manages the assignment of the Public IP Address to the FQDN.
   Enterprises only have to provide the Private IP Address. 

-  Alkira provides the NAT capability for incoming traffic from the
   Public IP to Private IP of the IFA

-   For a Cloud DMZ like environment, the network admin can also
   configure a policy for Firewall inspection of the application traffic
   to provide additional security measures.

How can the Internet-facing application be accessed?

Enterprises can have an Enterprise DNS server which is used by their
clients. On this Enterprise DNS server the Enterprise cancould create
CName and map their FQDN to the Alkira provided FQDN. 

For example, say the app has an Aalkira provided FQDN as
'`app1.mycompany.apps.alkira.com <http://app1.mycompany.apps.alkira.com>`__'.
This can be mapped to
'`app1.mycompany.com <http://app1.mycompany.com>`__' and used by the
Enterprise users.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image3.png
   :alt: https://lh7-us.googleusercontent.com/Yb2sz9MF5A3IGf7ZX_mg3M7SdcEVGgjtyQmCVKpQgegpvu7n_2ncgTrg1ViysJp0maicnj3ttriDzPLI12hafuL6HUux25qV9L6LDri2t2BQh3QWApKHPBlSntFT-e-oFVLazwOzSP9vzM3RwTMN_xM
   :width: 6.5in
   :height: 2.92708in

How to visualize the provisioned applications?

The green bars on the dashboard indicate the provisioned applications.
Hover on these bars to view the application details. 

How are the Internet facing applications categorized?

These applications are divided into the following three sizes based upon
the number of concurrent sessions they can accommodate:

-  Small 1000 sessions

-  Medium 5000 sessions

-  Large 10000 sessions

Configure Internet Facing Applications

Follow the steps below to configure an internet-facing application:

1. Navigate to
   |https://lh7-us.googleusercontent.com/p5ZewrgD6wi-g05mVqSK88rCDZTshfSgdpMNIhCwaCbyUpgMUqitxdY6DWEpCpdJalzY3IKP6_Nkc9E84hJH_MYn5iR3xenTHMVlUAQigzh2bKt--oKGu7CbzXbKpktvosMW4UmRotOQ9wqwqHA1ojs|
   **Applications** in the side menu. Then, click  the
   |https://lh7-us.googleusercontent.com/cz3R5hzI00URdMKJtgKXe5TxnksrOs0dLf51NvKWEHvvV-4uoNkUzeqwPmtEDQbbwrjE-RDvO8E0AF9qkukZ9y2uZVPtVWfMLdnilS0wkNKz01PCYeBJa2GxwVP3OM6lhrJw2ziUupKLFBTnoHDRoH8|
   button located at the top right corner of the UI. The following view
   will appear on the screen. 

1. Specify the following information  to add a new application. 

a. **Application Name:** The name of the application. Names can **only**
      be alphanumeric characters.

b. **Description-** This is a text field where a description of the
      Internet facing Application can be entered. This is an optional
      field. 

c. **Application accessed via Akamai Prolexic connector –** Set the
      toggle button to **Yes** to enable the Akamai Prolexic support.
      Refer to `Akamai Prolexic Support in
      IFA <https://docs.google.com/document/d/1oiXUhVFua_zO3KmJNKNUUN53FlPJspWwKN89Ip8b2nU/edit?pli=1#heading=h.wtkv1s2ltivc>`__
      section for more updates.

d. **FQDN Prefix**: The FQDN prefix for the application that will be
      used to assign an Alkira DNS to the application. This is a
      required field.

e. **IP address type for FQDN:** Set the toggle to **IPv4**, **IPv6**,
      or **Both** as per your requirement. It is used for mapping FQDN.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image6.png
   :alt: https://lh7-us.googleusercontent.com/W2T7QC7HEbAJ7kewp6C0rbBLSHwameZOY4Kv6vBCygROxVhIeD9XPsuY3Pl8HaxmzLGDvJ4hyw0EItHorH87DqQ6QXjZz95eKyMwkGN3vYsVIwez16RUG-zSrbq4a4BHMGVUailokWeua260oHoZyjQ
   :width: 6.5in
   :height: 3.32292in

**Note**: In case of **IPv6** or **both**, navigate to the Management →
Segments to configure the IPv6 to IPv4 NAT pool. For more details refer
to `Manage
Segments <https://docs.google.com/document/d/1oiXUhVFua_zO3KmJNKNUUN53FlPJspWwKN89Ip8b2nU/edit?pli=1#heading=h.ryhs6nmylhlo>`__
section.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image7.png
   :alt: https://lh7-us.googleusercontent.com/pj7RphjmBvkJoQbQIM17RnxCdFifSiX3hLjN9sfKN5Pjq3U4-NZeaAg5VZXLDptIS97-qYLf-tVm721lVdmwJZKWVQCPwKIYsvbMo82dqj4zrBG0SE3kXDQftSCFDnOiNTlBMb4apL1c_b_m7EQTbdQ
   :width: 6.5in
   :height: 2.23958in

f. | **Source NAT IPv4 traffic:** Mark the checkbox to enable IPv4 NAT
        on source traffic. Once enabled, two additional fields pop up
        where you define an address range to configure IPv4 to IPv4 NAT
        Pool for IFA. The NAT pool size is 128 addresses.
      | |https://lh7-us.googleusercontent.com/ccofdchyBB9nwrN0Uv7i0c3AEpLXLrL5DHFyLc8f-TPPXZCVMxf6uV14pmO9tnlreUuQqISSL2k9HB8aIxwSGD7K-y4Dx13Pl2LVOSXqBYVYbtQ4rEGweMkgyYzzHC3oS7sFnCFnFho_I1l_cybGrQM|

..

   **Note:** Ensure that the NAT pool doesn’t overlap with network
   addresses used on-premise or in the cloud for the associated segment.

When hosting an IFA in a data center or cloud environment, where the
customer's network directs traffic towards the internet by default,
enabling Source NAT for IPv4 Traffic is crucial. This prevents potential
traffic loss, as traffic might inadvertently take the default route and
not return to the CXP. By checking the Source NAT IPv4 Traffic box in
the configuration settings and providing IPv4 Start and End Addresses,
you can map your public IP address to the NATed IP address. For the
outbound traffic Alkira will route the traffic based on the destination
IP address without performing source port mapping. Alkira maintains a
mapping of the source IP address for each AZ to route the reverse
traffic flow correctly. This approach ensures proper traffic routing and
prevents loss of traffic.

g. **Enable Bi-directional IFA Traffic:** You can enable bi-directional
      traffic for IFA configured. With this option enabled, the server
      can source the traffic to a public destination. Note that there is
      only a single Availability Zone when choosing this option so that
      the same IFA IP address can be used for the flow initiated by the
      application. Any internet traffic from the server will be sent out
      to the internet using IFA IP instead of Internet Connector in that
      segment. Note that Source NAT cannot be configured with
      Bi-Directional IFA Traffic and AWS LoadBalancer cannot be
      application destination.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image9.png
   :alt: https://lh7-us.googleusercontent.com/RgAF9-lAx4b1BOhmjZrzBWC8z-AgXoWwRGMfNBYDjm1vzubnSaRjHoAapkaBNj-KSdDvqyJ0tqzzxxz7BinBV5ghxfwhdoHXB38Fu3iajf3VGTHNYH-l8uwfP3TRT4gKUzPGYSN1ow47iTwfV_3BnGE
   :width: 6.5in
   :height: 3.53125in

To ensure that traffic can be initiated from either the user or
application side and always received at the known source IP address,
enable Bi-directional IFA Traffic. By checking this box, Alkira removes
the redundancy of the Availability Zones so that traffic always maps to
the same AZ, whether it's Alkira's or the customer's EIP. With only one
AZ, there is only one IP address, simplifying routing as Alkira doesn't
need to perform any port changes. Incoming traffic is directed to the
application via DNAT, and return traffic goes back to the CXP, with the
source IP becoming the destination IP for steering back to the same AZ.

When traffic is initiated from the Application’s perspective, the flow
is slightly different. To ensure that return traffic comes back to the
CXP, any traffic originating from the application VPC will go through
the CXP (not the internet connector) if the Enable Bi-directional IFA
Traffic box is checked. Alkira performs NATing on the source IP to its
EIP before sending traffic out to the internet. This allows Alkira to
identify and route the traffic back to its own CXP and perform DNAT to
the application IP for the reverse traffic flow.

h. **Use BYOIP Address for FQDN:** Select **Yes** to enable this
      functionality. In the additionaladditonal pop up fields, select
      your BYOIP Prefix from the dropdown and specify your public IP
      addresses accordingly.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image10.png
   :alt: https://lh7-us.googleusercontent.com/y2LP3B8iZwsbaxkjRPJddCwm6neA9EO4FSB1iQTW-5_ZbSImiZi5YUR6HoyaTr7KN58LlMXYtQMcAqVHAkvkhpGRBayUXfSs8ptWdhr4PCsWW8ywU3Sp4qEcxiwFGUIu2rEI9crX0PoUXh6gO9SyZCM
   :width: 6.5in
   :height: 1.91667in

   **Note: BYOIP** only supports IPv4 addressesaddress. Enabling
   **BYOIP** will disable the **IPv6** option. For more details, refer
   to
   `BYOIP <https://docs.google.com/document/d/1oiXUhVFua_zO3KmJNKNUUN53FlPJspWwKN89Ip8b2nU/edit?pli=1#heading=h.vbo3q8xrr5p0>`__
   section. 

i. **Source NAT IPv4 traffic:** Mark the checkbox to enable IPv4 NAT on
      source traffic. Once enabled, two additional fields pop up where
      you define an address range to configure IPv4 to IPv4 NAT Pool for
      IFA. The NAT pool size is 128 addresses.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image11.png
   :alt: https://lh7-us.googleusercontent.com/Dhuh5wuYvG61NwhLh-RDrpmW6Z_dIpHvpQ-bNMSFr5cCrFw0WL1fpu3zJ11C7zzutObMeqZMy1Sz4D4sPbz1GSrmBipRg9tArZjylYgSVQGD1dLn7_f0pafZ2zz2HdHZVoY83hn94oMD_5zyJdmFAKU
   :width: 6.5in
   :height: 1.41667in

   **Note:** Ensure that the NAT pool doesn’t overlap with network
   addresses used on-premise or in the cloud for the associated segment.

   **j.** Specify the following connector details in the connector
   association section.

a. **Connector Type:** Select the type of connector to be associated
      with the application from the dropdown. Alkira currentlycurrenlty
      supports  IPsec, AWS, Azure, GCP and AWS DX. This depends upon the
      location of where the application is hosted. This is a required
      field.

..

   **Note: ** If the connector type is **AWS,** you can choose to enable
   Hosted Internal Load Balancer (ILB) to increase the capacity and
   reliability of your application. Refer to `Internal Load Balancer
   (ILB) <https://docs.google.com/document/d/1oiXUhVFua_zO3KmJNKNUUN53FlPJspWwKN89Ip8b2nU/edit?pli=1#heading=h.iz1cj7y54gfe>`__
   for more details.

b. **Select connector**: Based on connector type, select the existing
      connector.

a. **Select size:** Specify your connector size from the dropdown menu.

a. **Private IP Address:** The IP address of the application.

a. **Port:** The port used to access the application. Specify the port
   number(s) between 1-655345  or a port range with comma-separated
   values.  

**            k. Use BYOIP Address for FQDN:** Select **Yes** to enable
this functionality. In the additional pop up fields, select your BYOIP
Prefix from the dropdown and specify your public IP addresses
accordingly.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image10.png
   :alt: https://lh7-us.googleusercontent.com/y2LP3B8iZwsbaxkjRPJddCwm6neA9EO4FSB1iQTW-5_ZbSImiZi5YUR6HoyaTr7KN58LlMXYtQMcAqVHAkvkhpGRBayUXfSs8ptWdhr4PCsWW8ywU3Sp4qEcxiwFGUIu2rEI9crX0PoUXh6gO9SyZCM
   :width: 6.5in
   :height: 1.91667in

**Note: BYOIP** only supports IPv4 addresses. Enabling **BYOIP** will
disable the **IPv6** option. For more details, refer to
`BYOIP <https://docs.google.com/document/d/1oiXUhVFua_zO3KmJNKNUUN53FlPJspWwKN89Ip8b2nU/edit?pli=1#heading=h.vbo3q8xrr5p0>`__
section.

f. **Billing Tag:** The billing tag to be associated with the
      application usage. You can also create a billing tag by clicking
      on the plus icon
      |https://lh7-us.googleusercontent.com/2yKkFh6rrm8HiqZ0iwHzAoUERngI-2vr70WcP6P4ILJIZPf00bPfjDVBv6-QKmrukkI6CQRRE8UTmmbh46BboUfJNKbrOOVUSC7MDOB9LFir2xmA7bl1szPIOfWewUj-YJGcxb3xfNqhCZTpuplxj8A|.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image13.png
   :alt: https://lh7-us.googleusercontent.com/RdiO4sjU2ROIdu4nsIX0ARyfV3Qjd5V8cIcM1oVHjVWuBc0hHda2cEfl7QDgxGE8c7YxgkGjUYA7QvHgfT30o5w1DZFqTXWFIGJjHevKz8s8EEyeaMVsVNVsN2MeK3n2_NEXZRf3yj56UUe1sTT7OqE
   :width: 6.5in
   :height: 3.25in

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image9.png
   :alt: https://lh7-us.googleusercontent.com/RgAF9-lAx4b1BOhmjZrzBWC8z-AgXoWwRGMfNBYDjm1vzubnSaRjHoAapkaBNj-KSdDvqyJ0tqzzxxz7BinBV5ghxfwhdoHXB38Fu3iajf3VGTHNYH-l8uwfP3TRT4gKUzPGYSN1ow47iTwfV_3BnGE
   :width: 6.5in
   :height: 3.53125in

**Note:** You can enable bi-directional traffic for IFA configured. With
this option enabled, the server can source the traffic to a public
destination. Note that there is only a single Availability Zone when
choosing this option. Any internet traffic from the server will be sent
out to the internet using IFA IP instead of Internet Connector in that
segment. Note that Source NAT cannot be configured with Bi-Directional
IF Traffic and AWS LoadBalancer cannot be application destination.  

    Select **Save Application**. A dialog box will appear on the screen
   indicating the application creation status. The next step is to add a
   policy for this application.

   .. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image14.png
      :alt: https://lh7-us.googleusercontent.com/MZ2hzskIpHT8YO1vuszIF9q0HMffsyc4TlrqSDJXcOR7ybULLwPu8VF6eS66kVYcZSIp5xDgn3nn6i3H-FOrKDYy9VTBcHZdYcjuZt1t5wIrFXcItZBonjWpSnPL55KXXRGQQsczkRDonr2xqd113jc
      :width: 6.5in
      :height: 3.33333in

4. By default, the Alkira portal blocks all the traffic to IFA. After
creating the application, a policy needs to be implemented. Refer to the
`Policies <https://docs.google.com/document/d/1oiXUhVFua_zO3KmJNKNUUN53FlPJspWwKN89Ip8b2nU/edit?pli=1#heading=h.nlmz8ecoefm2>`__
section for more details.

5. The final step for an internet-facing application is to provision it.
Refer to the
`Provision <https://docs.google.com/document/d/1oiXUhVFua_zO3KmJNKNUUN53FlPJspWwKN89Ip8b2nU/edit?pli=1#heading=h.tzwavyjbsvnb>`__
section for more details. 

Once provisioned, it appears as tabular data in the **Internet Facing
Applications** panel. Click on a specific application to view its
metadata.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image15.png
   :alt: https://lh7-us.googleusercontent.com/ZcPCjB3kUHh0GiMOwQCzEe7iE3LOQu7oxpctktcxfrLBhHNJxwVWahcUZEtO6jjn-tLWmh2rIoB0Q7x_B4d6MA_DjitYH8Q9j8_gg_6eHkkt49NQwMUcp1UQ60lixvLhW6RpXP0ylGtT2iafukq7AuE
   :width: 6.5in
   :height: 3.125in

   Akamai Prolexic Support in IFA

   Once you choose to access the application via Akamai Prolexic
   Connector, specify the following fields:

-  **Select Ingress Akamai Connector –** Select a connector from the
      dropdown menu.

-  **Public IP Address1 –** Specify public IP Address 1 for the IFA
      application. It must be part of the BYOIP range selected in the
      Akamai Prolexic Connector.

-  **Public IP Address 2 –** Specify public IP Address 2 for the IFA
      application. It must be part of the BYOIP range selected in the
      Akamai Prolexic Connector. **Ports (1-65535) –** Specify a port
      number for your application. 

-  **Select Destination Connector Type –** Specify a connector type for
      the application server.

-  **Destination Connector**: Select from the range of connectors in the
      dropdown menu for specified type. 

-  **Private IP Address –** The IP address for the application server.

-  **Billing Tag**: The billing tag to be associated with the
      application usage. You can also create a billing tag by clicking
      on the plus icon
      |https://lh7-us.googleusercontent.com/2yKkFh6rrm8HiqZ0iwHzAoUERngI-2vr70WcP6P4ILJIZPf00bPfjDVBv6-QKmrukkI6CQRRE8UTmmbh46BboUfJNKbrOOVUSC7MDOB9LFir2xmA7bl1szPIOfWewUj-YJGcxb3xfNqhCZTpuplxj8A|.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image16.png
   :alt: https://lh7-us.googleusercontent.com/cWNh9wBbwkg6-60OkheqyX3VcHBfzJVFTuQ8AtsT5GTn6iVLF0XC4CEsC7KIgF9ZfBaqBi7pqiAK4VlWvQFIAGxQZVLpwYQG_6-LCtN5DmtERUUIAJYkcqssPsqjwpxUoe5_qx3GvAh1-HZSqfxIhUw
   :width: 6.5in
   :height: 3.33333in

   Internal Load Balancer (ILB)

**Note:** This option is only visible if the associated connector type
is **AWS.**

   If the application is hosted in AWS behind an Internal Load Balancer
   (ILB) inside of a VPC already onboarded on Alkira, users can
   configure the ILB as the destination for traffic destined to the IFA.
   Alkira will monitor the status of the servers in the target group
   associated with the ILB and load balance the inbound connections to
   the available servers behind the ILB. Alkira will use the previously
   provided AWS credential and retrieve the list of available ILB’s in
   the VPC the user can select from.

   Set the toggle button to **YES** to configure the Internal Load
   Balancer (ILB). An additional field named **Load Balancer** appears.
   Select the desired load balancer from the list of available ILBs in
   the specific VPC. Then configure the ports the application will
   listen on.

   **Note**: Update AWS IAM Policy to fetch the ILB’s. The following
   actions must be allowed in the IAM policy: "Action":
   "elasticloadbalancing:DescribeLoadBalancers”. This also helps Alkira
   to consolidate all Egress and Ingress traffic through CXP.

   For Azure and GCP connectors, the configuration of ILBs is not
   required since both provide redundancy by default. 

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image17.png
   :alt: https://lh7-us.googleusercontent.com/cXRiEf15BoIHnOvaJoWM-Mdj91rj23Bvzu3NXq3dGcwwDHPgjfWC8Jh3jEHkJklFc5hWDMKd2_Sd3FPiZAXRewV_gXRdzeV6qZdcCX8faKRvoP1XOLNMAEw6RcmGZPkN8ttqQb6MlxmuKsDboe8HXK0
   :width: 6.5in
   :height: 3.125in

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image18.png
   :alt: https://lh7-us.googleusercontent.com/jNWnxjPBoeIASfPp1jsTW2TTv4F5Ti351dqAf5q4hZcZglNvprKe66Xg7XhHM6V09Ld9fcdkyOp2Yt4WhrpZSiFkd5xk0iIkDKiUSXKuCrRs4MV66Cb9FCF4j4VD4Veo9wi1s2X1O60tUqsw7XxP_SI
   :width: 6.5in
   :height: 3.08333in

**Monitor Internet Facing Applications
**\ Alkira portal dashboard provides high-level statistics related to
the internet-facing applications. It displays the following information
for the IFAs:

-  Top applications based upon their usage

-  Application utilization in MBs/GBs

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image19.png
   :alt: https://lh7-us.googleusercontent.com/_ytjweiADIMnFOEeyxI9gnksWA5vAa-Bfl-S21q1ktk0ragxcDnNXjcUMdtsUiUedo1BwNQBg-CXAmE-uJD-dgG8-VvDRMj2Al7osY1YJz7RurSScVtP126jrPgcVY71YRYxIT-SX3fEnPSv6CaGCPw
   :width: 6.5in
   :height: 3.33333in

For further information on the detailed bandwidth utilization, session
count, etc. of the applications, navigate to **Dashboard**
|https://lh7-us.googleusercontent.com/9j2tAHRS_6tR6aM3qc5oLxnrflTzvuHUV8xMMdGbwVISoh2QMGji9KhZcXYe9gudDpsD1gZ0FTiiC6frwk9bwKMIi5iyB5CRISza1hj-iANZa8jSvUzlKUzg14GOKJ-_G2a5hrZKWcaUxebYb2mCdI8|
from the left navigation sidebar and locate **Applications**. The
following view will appear on the screen displaying IFA details.

.. image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image21.png
   :alt: https://lh7-us.googleusercontent.com/wrMSQyOsqcjaFNmd9WswW7XyAs4PVdH6gDxjfaPeBpPwjwNZZj65uyxoN3k_kKxeygVR1qPIvFYjv_EnQbxeDKQzHmMJ_OGTKz8NfHd9ssgBRlBe2_YaNo4Re6c_GUqkpKgNenNROcn3W8MrGO7uC1U
   :width: 6.5in
   :height: 3.125in

.. |https://lh7-us.googleusercontent.com/syFrus3YO7kSToMYupHc7njrFqW-mB17l0JgPUyo5fIIFFZfmya8MwV-VbYsNYbQu946zpTIPw1moBhmch6VMHMcDUZVk111pAb2iG2qJCYuzKbI16VF-hQbK2uxIV__moJ3BhIdbxtF1lHzQgKhVJs| image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image1.png
   :width: 0.20833in
   :height: 0.23958in
.. |https://lh7-us.googleusercontent.com/p5ZewrgD6wi-g05mVqSK88rCDZTshfSgdpMNIhCwaCbyUpgMUqitxdY6DWEpCpdJalzY3IKP6_Nkc9E84hJH_MYn5iR3xenTHMVlUAQigzh2bKt--oKGu7CbzXbKpktvosMW4UmRotOQ9wqwqHA1ojs| image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image4.png
   :width: 0.52083in
   :height: 0.4375in
.. |https://lh7-us.googleusercontent.com/cz3R5hzI00URdMKJtgKXe5TxnksrOs0dLf51NvKWEHvvV-4uoNkUzeqwPmtEDQbbwrjE-RDvO8E0AF9qkukZ9y2uZVPtVWfMLdnilS0wkNKz01PCYeBJa2GxwVP3OM6lhrJw2ziUupKLFBTnoHDRoH8| image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image5.png
   :width: 0.27083in
   :height: 0.26042in
.. |https://lh7-us.googleusercontent.com/ccofdchyBB9nwrN0Uv7i0c3AEpLXLrL5DHFyLc8f-TPPXZCVMxf6uV14pmO9tnlreUuQqISSL2k9HB8aIxwSGD7K-y4Dx13Pl2LVOSXqBYVYbtQ4rEGweMkgyYzzHC3oS7sFnCFnFho_I1l_cybGrQM| image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image8.png
   :width: 6.5in
   :height: 3.25in
.. |https://lh7-us.googleusercontent.com/2yKkFh6rrm8HiqZ0iwHzAoUERngI-2vr70WcP6P4ILJIZPf00bPfjDVBv6-QKmrukkI6CQRRE8UTmmbh46BboUfJNKbrOOVUSC7MDOB9LFir2xmA7bl1szPIOfWewUj-YJGcxb3xfNqhCZTpuplxj8A| image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image12.png
   :width: 0.27083in
   :height: 0.28125in
.. |https://lh7-us.googleusercontent.com/9j2tAHRS_6tR6aM3qc5oLxnrflTzvuHUV8xMMdGbwVISoh2QMGji9KhZcXYe9gudDpsD1gZ0FTiiC6frwk9bwKMIi5iyB5CRISza1hj-iANZa8jSvUzlKUzg14GOKJ-_G2a5hrZKWcaUxebYb2mCdI8| image:: vertopal_fdf600e7cffd4b6ebb0c02f4232d8033/media/image20.png
   :width: 0.20833in
   :height: 0.22917in
