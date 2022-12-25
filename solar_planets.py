import cv2
img=cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (125,185),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (195,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (0,255,0)
            )

cv2.putText(img,
            "Tierra",
            (292,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Marte",
            (385,270),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (0,255,0)
            )

cv2.putText(img,
            "Jupiter",
            (590,60),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturno",
            (780,110),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (0,255,0)
            )

cv2.putText(img,
            "Urano",
            (975,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptuno",
            (1120,130),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (0,255,0)
            )

cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)

